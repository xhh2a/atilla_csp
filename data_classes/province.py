from enum import Enum
from collections import defaultdict
from funcy import flatten
from pydantic import BaseModel, Field, model_validator
from typing import Optional

from data_classes.types import Modifier, ModifierType, VariableType


class BuildingChain(str, Enum):
    CITY = "city"
    TOWN = "town"
    RELIGION_1 = "religion_1"
    RELIGION_2 = "religion_2"
    FARMING_1 = "farming_1"
    FARMING_2 = "farming_2"
    FARMING_3 = "farming_3"
    FARMING_4 = "farming_4"


class BuildingLocation(str, Enum):
    ANY = "any"
    CITY = "city"
    TOWN = "town"
    ALCOVE = "alcove"


class Building(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory=lambda: [])
    chain: BuildingChain
    building_location: Optional[BuildingLocation] = BuildingLocation.ANY


class Settlement(BaseModel):
    total_slots: int = 0
    has_port: bool = False
    trade_good_building: Optional[Building] = None
    need_garrison: bool = False
    buildings: Optional[list[Building]] = Field(default_factory=lambda: [])

    @property
    def modifiers(self):
        return list(flatten([building.modifiers for building in self.buildings]))


class City(Settlement):
    total_slots: int = 5


class Town(Settlement):
    total_slots: int = 3


class Province(BaseModel):
    fertility: int = 0
    """
    Net fertility from misc sources
    """
    city: City = Field(default_factory=lambda: City())
    towns: list[Town] = Field(default_factory=lambda: [Town(), Town()])

    def check_basic_constraints(
        self,
        current_public_order: int = 0,
        current_food: int = 0,
        current_sanitation: int = 0,
    ):
        for settlement in [self.city, *self.towns]:
            for modifier in settlement.modifiers:
                match modifier.variable:
                    case VariableType.FOOD:
                        current_food += modifier.get_effective_value(self.fertility)
                    case VariableType.SANITATION:
                        current_sanitation += modifier.get_effective_value(
                            self.fertility
                        )
                    case VariableType.PUBLIC_ORDER:
                        current_public_order += modifier.get_effective_value(
                            self.fertility
                        )
        if current_food < 0 or current_sanitation < 0 or current_public_order < 0:
            raise ValueError("Invalid combination")
        return self

    def get_province_value(
        self,
        public_order: int = 0,
        food: int = 0,
        sanitation: int = 0,
        tax_rate: float = 1.0,
        corruption: float = 0.5,
        existing_modifiers=None,
    ):
        self.check_basic_constraints(
            current_public_order=public_order,
            current_food=food,
            current_sanitation=sanitation,
        )
        current_income_values = {
            income_type: 0 for income_type in VariableType.income_types
        }
        current_income_modifiers = defaultdict(float)
        all_modifiers = [
            *existing_modifiers,
            *[settlement.modifiers for settlement in [self.city, *self.towns]],
        ]
        for modifier in all_modifiers:
            if modifier.variable in VariableType.income_types:
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
            elif modifier.variable in VariableType.income_modifiers:
                current_income_modifiers[
                    modifier.variable
                ] += modifier.get_effective_value(self.fertility)
        resource_income_value = 0
        for income_type, raw_income_value in current_income_values.items():
            income_percent_modifier = current_income_modifiers.get(income_type, 0.0)
            income_percent_modifier += current_income_modifiers.get(
                VariableType.ALL_INCOME
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
