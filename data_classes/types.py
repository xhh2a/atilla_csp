from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class VariableType(str, Enum):
    # Core
    FOOD = "food"
    PUBLIC_ORDER = "public_order"
    SANITATION = "sanitation"
    FAITH = "faith"
    ALTERNATE_FAITH = "alternate_faith"
    GROWTH = "growth"

    # Misc
    RESEARCH = "research"
    TRADE_INCOME = "trade_income"
    CONSTRUCTION_COST = "construction_cost"

    # Money
    CULTURE = "culture"
    COMMERCE = "commerce"
    INDUSTRY = "industry"
    FARMING = "farming"
    SUBSISTENCE = "subsistence"
    ALL_INCOME = "income"
    TAX_RATE = "tax_rate"  # Immigration is basically tax rate.
    CORRUPTION = "corruption"

    # Military
    REPLENISHMENT = "replenishment"
    RECRUITMENT_CAPACITY = "recruitment_capacity"
    GARRISON = "garrison"
    ROAD = "road"

    # Equipment
    UNIT_ENABLE = "enable_unit"
    UNIT_SPEED = "unit_speed"
    UNIT_MORALE = "unit_morale"
    UNIT_ARMOR = "unit_armor"
    UNIT_DEFENSE = "unit_defense"
    UNIT_ATTACK = "unit_attack"
    UNIT_DAMAGE = "unit_damage"
    UNIT_SHIELD = "unit_shield"
    UNIT_LEVEL = "unit_level"
    UNIT_AMMO = "unit_ammo"

    # Agent
    AGENT_ENABLE = "enable_agent"
    AGENT_CAP = "agent_cap"
    AGENT_LEVEL = "agent_level"

    @classmethod
    def income_types(cls):
        return {cls.FARMING, cls.CULTURE, cls.COMMERCE, cls.SUBSISTENCE, cls.INDUSTRY}

    @classmethod
    def income_modifiers(cls):
        return {cls.ALL_INCOME, cls.TAX_RATE, cls.CORRUPTION}


class ModifierType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"  # Additive Percentage
    FERTILITY = "fertility"


class ModifierLocation(str, Enum):
    PROVINCE = "province"
    SETTLEMENT = "settlement"
    ADJACENT = "adjacent"
    GLOBAL = "global"


class Modifier(BaseModel):
    type: ModifierType
    variable: VariableType
    sub_category: Optional[Any] = None  # Not used currently
    location: Optional[ModifierLocation] = ModifierLocation.PROVINCE
    value: Any

    def get_effective_value(self, fertility: int):
        if self.type == ModifierType.FERTILITY:
            return self.value * fertility
        else:
            return self.value


class Edict(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory=lambda: [])


class UnitType(str, Enum):
    CAVALRY = "cavalry"
    INFANTRY = "infantry"
    RANGED = "ranged"
    NAVAL = "naval"
    LAND = "land"


class AgentType(str, Enum):
    ALL = "all"
    PRIEST = "priest"
    CHAMPION = "champion"
    SPY = "spy"


class ReligionType(str, Enum):
    SEMETIC_PAGANISM = "semetic_paganism"
    EASTERN_CHRISTIANITY = "eastern_christianity"
    GERMANIC_PAGANISM = "germanic_paganism"
