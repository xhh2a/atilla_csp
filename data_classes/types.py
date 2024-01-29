from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class Variable(str, Enum):
    # Core
    FOOD = "food"
    PUBLIC_ORDER = "public_order"
    SANITATION = "sanitation"
    FAITH = "faith"
    ALTERNATE_FAITH = "alternate_faith"

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

    # Agent
    AGENT_ENABLE = "enable_agent"
    AGENT_CAP = "agent_cap"
    AGENT_LEVEL = "agent_level"


class ModifierType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"  # Additive Percentage
    FERTILITY = "fertility"


class Location(str, Enum):
    PROVINCE = "province"
    SETTLEMENT = "settlement"
    ADJACENT = "adjacent"


class Modifier(BaseModel):
    type: ModifierType
    variable: Variable
    sub_category: Optional[Any] = None  # Not used currently
    location: Optional[Location] = Location.PROVINCE
    value: Any


class Edict(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory=lambda : [])


class AgentType(str, Enum):
    PRIEST = "priest"
    CHAMPION = "champion"
    SPY = "spy"

class ReligionType(str, Enum):
    SEMETIC_PAGANISM = "semetic_paganism"
    EASTERN_CHRISTIANITY = "eastern_christianity"


