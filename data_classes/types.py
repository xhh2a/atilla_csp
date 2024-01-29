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

    # Money
    CULTURE = "culture"
    COMMERCE = "commerce"
    INDUSTRY = "industry"
    FARMING = "farming"
    SUBSISTENCE = "subsistence"
    INCOME = "income"
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

    # Agent
    AGENT_ENABLE = "enable_agent"
    AGENT_CAP = "agent_cap"
    AGENT_LEVEL = "agent_level"


class ModifierType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"  # Additive Percentage
    FERTILITY = "fertility"


class ModifierLocation(str, Enum):
    PROVINCE = "province"
    SETTLEMENT = "settlement"
    ADJACENT = "adjacent"


class Modifier(BaseModel):
    type: ModifierType
    variable: VariableType
    sub_category: Optional[Any] = None  # Not used currently
    location: Optional[ModifierLocation] = ModifierLocation.PROVINCE
    value: Any


class Edict(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory=lambda : [])


class UnitType(str, Enum):
    CAVALRY = "cavalry"
    INFANTRY = "infantry"
    RANGED = "ranged"

class AgentType(str, Enum):
    PRIEST = "priest"
    CHAMPION = "champion"
    SPY = "spy"

class ReligionType(str, Enum):
    SEMETIC_PAGANISM = "semetic_paganism"
    EASTERN_CHRISTIANITY = "eastern_christianity"


