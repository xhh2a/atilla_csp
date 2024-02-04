from enum import Enum
from collections import defaultdict
from funcy import flatten
from pydantic import BaseModel, Field, model_validator
from typing import Annotated, Any, Optional
from configuration import ContextVariableKeys, get_context
from warnings import warn

from data_classes.types import Modifier, ModifierLocation, ModifierType, VariableType


class BuildingChain(str, Enum):
    CITY = "city"
    TOWN = "town"
    RELIGION_1 = "religion_1"
    RELIGION_2 = "religion_2"
    FARMING_WHEAT = "farming_1"
    FARMING_CAMEL = "farming_2"
    FARMING_STABLES = "farming_3"
    FARMING_SHEEP = "farming_4"
    INDUSTRY_CONSTRUCTION = "industry_construction"
    INDUSTRY_CULTURE = "industry_culture"
    INDUSTRY_COMMERCE = "industry_commerce"
    INDUSTRY_MONEY = "industry_money"
    INDUSTRY_RANGED = "industry_ranged"
    INDUSTRY_ARMOR = "industry_armor"
    INDUSTRY_PLEASURE = "industry_pleasure"
    WATERWORKS = "waterworks"
    TRADE_MARKET = "trade_market"
    FOOD_MARKET = "food_market"
    SLAVE_MARKET = "slave_market"
    RESEARCH = "research"
    CIVIC_CENTER = "civic_center"
    PORT = "port"
    TRADE_RESOURCE = "trade_resource"


class BuildingLocation(str, Enum):
    ANY = "any"
    CITY = "city"
    TOWN = "town"
    ALCOVE = "alcove"


class Building(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory=list)
    chain: BuildingChain
    building_location: Optional[BuildingLocation] = BuildingLocation.ANY


class Settlement(BaseModel):
    total_slots: int = 0
    has_port: bool = False
    trade_good_buildings: Annotated[list[Building], Field(default_factory=list)]
    buildings: Annotated[list[Building], Field(default_factory=lambda: [])]
    need_garrison: bool = False

    @property
    def free_slots(self):
        return self.total_slots - len(self.buildings)

    @property
    def existing_building_chains(self):
        return [building.chain for building in self.buildings]

    @property
    def is_complete(self):
        return self.free_slots == 0

    @property
    def modifiers(self):
        return list(flatten([building.modifiers for building in self.buildings]))


class City(Settlement):
    total_slots: int = 6

    @model_validator(mode="after")
    def main_settlement(self):
        main_city_building = get_context(ContextVariableKeys.CITY_BUILDING)
        if main_city_building is not None and not any(
            [building.chain == BuildingChain.CITY for building in self.buildings]
        ):
            self.buildings.append(get_context(ContextVariableKeys.CITY_BUILDING))
        if main_city_building is None:
            warn("City object initialized before data was loaded for a specific faction. Consider saving inputs as a dict until after loading")
        return self

    @property
    def possible_buildings(self):
        if self.has_port and len(self.buildings) < 2:
            return get_context(ContextVariableKeys.PORT_BUILDINGS)
        elif len(self.buildings) >= self.total_slots:
            return set()
        return [
            building
            for building in [
                *get_context(ContextVariableKeys.CITY_BUILDING_OPTIONS),
                *self.trade_good_buildings,
            ]
            if building.chain not in self.existing_building_chains
        ]


class Town(Settlement):
    total_slots: int = 4

    @model_validator(mode="after")
    def main_settlement(self):
        main_town_building = get_context(ContextVariableKeys.TOWN_BUILDING)
        if main_town_building is not None and not any(
            [building.chain == BuildingChain.TOWN for building in self.buildings]
        ):
            self.buildings.append(main_town_building)
        if main_town_building is None:
            warn("Town object initialized before data was loaded for a specific faction. Consider saving inputs as a dict until after loading")
        return self

    @property
    def possible_buildings(self):
        if self.has_port and len(self.buildings) < 2:
            return get_context(ContextVariableKeys.PORT_BUILDINGS)
        elif self.is_complete:
            return set()
        return [
            building
            for building in [
                *get_context(ContextVariableKeys.TOWN_BUILDING_OPTIONS),
                *self.trade_good_buildings,
            ]
            if building.chain not in self.existing_building_chains
        ]


INCOME_TYPES = VariableType.income_types()
INCOME_MODIFIERS = VariableType.income_modifiers()


class Province(BaseModel):
    fertility: int = 0
    """
    Net fertility from misc sources
    """
    city: City = Field(default_factory=lambda: City())
    first_town: Town = Field(default_factory=lambda: Town())
    second_town: Town = Field(default_factory=lambda: Town())
    _province_sanitation: Any = None
    _local_sanitation: Any = None
    _food: Any = None
    _public_order: Any = None

    @property
    def towns(self):
        return [self.first_town, self.second_town]

    def get_missing_resource(
        self,
        current_public_order: int = 0,
        current_food: int = 0,
        current_sanitation: int = 0,
    ):
        local_sanitations = []
        province_sanitation = current_sanitation
        for settlement in [self.city, *self.towns]:
            local_sanitation = 0
            for modifier in settlement.modifiers:
                match modifier.variable:
                    case VariableType.FOOD:
                        current_food += modifier.get_effective_value(self.fertility)
                    case VariableType.SANITATION:
                        if modifier.location == ModifierLocation.PROVINCE:
                            province_sanitation += modifier.get_effective_value(
                                self.fertility
                            )
                        else:
                            local_sanitation += modifier.get_effective_value(
                                self.fertility
                            )
                    case VariableType.PUBLIC_ORDER:
                        current_public_order += modifier.get_effective_value(
                            self.fertility
                        )
            local_sanitations.append(local_sanitation)

        self._food = current_food
        self._public_order = current_public_order
        self._local_sanitations = local_sanitations
        self._province_sanitation = province_sanitation
        if current_food < 0:
            return VariableType.FOOD
        if current_public_order < 0:
            return VariableType.PUBLIC_ORDER
        if any(
            [
                local_sanitation + province_sanitation < 0
                for local_sanitation in local_sanitations
            ]
        ):
            return VariableType.SANITATION
        return None

    def get_province_value(
        self,
        tax_rate: float = 1.0,
        corruption: float = 0.5,
        existing_modifiers=None,
    ):
        current_income_values = {income_type: 0 for income_type in INCOME_TYPES}
        current_income_modifiers = defaultdict(float)
        all_modifiers = flatten(
            [
                *(existing_modifiers or []),
                *[settlement.modifiers for settlement in [self.city, *self.towns]],
            ]
        )
        for modifier in all_modifiers:
            if modifier.variable in INCOME_TYPES:
                if modifier.type in {ModifierType.FLAT, ModifierType.FERTILITY}:
                    current_income_values[
                        modifier.variable
                    ] += modifier.get_effective_value(self.fertility)
                elif modifier.type == ModifierType.PERCENTAGE:
                    current_income_modifiers[
                        modifier.variable
                    ] += modifier.get_effective_value(self.fertility)
                else:
                    raise RuntimeWarning(f"Invalid modifier type: {modifier.type}")
            elif modifier.variable in INCOME_MODIFIERS:
                current_income_modifiers[
                    modifier.variable
                ] += modifier.get_effective_value(self.fertility)
        resource_income_value = 0
        for income_type, raw_income_value in current_income_values.items():
            income_percent_modifier = 1.0 + current_income_modifiers.get(
                income_type, 0.0
            )
            income_percent_modifier += current_income_modifiers.get(
                VariableType.ALL_INCOME, 0.0
            )
            resource_income_value += raw_income_value * income_percent_modifier
        tax_income = resource_income_value * (
            tax_rate + current_income_modifiers.get(VariableType.TAX_RATE, 0)
        )
        corruption_rate = corruption * (
            1.0 - current_income_modifiers.get(VariableType.CORRUPTION, 0)
        )
        received_income = tax_income * min(max((1.0 - corruption_rate), 0), 1.0)
        return received_income

    @property
    def is_complete(self):
        return all([town.is_complete for town in self.towns]) and self.city.is_complete
