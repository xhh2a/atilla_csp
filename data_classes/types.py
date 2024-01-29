from enum import Enum

from pydantic import BaseModel


class Variable(str, Enum):
    FOOD = "food"
    PUBLIC_ORDER = "public_order"
    SANITATION = "sanitation"
    CULTURE = "culture"
    COMMERCE = "commerce"
    INDUSTRY = "industry"
    FARMING = "farming"
    SUBSISTENCE = "subsistence"
    INCOME = "income"
    CORRUPTION = "corruption"


class ModifierType(str, Enum):
    FLAT = "flat"
    PERCENTAGE = "percentage"
    FERTILITY = "fertility"


class Modifier(BaseModel):
    type: ModifierType
    value: int
    variable: Variable