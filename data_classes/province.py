from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

from data_classes.types import Modifier


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
    modifiers: list[Modifier] = Field(default_factory = lambda: [])
    chain: BuildingChain
    building_location: Optional[BuildingLocation] = BuildingLocation.ANY


class Settlement(BaseModel):
    total_slots: int = 0
    has_port: bool = False
    trade_good_building: Optional[Building] = None
    need_garrison: bool = False


class City(Settlement):
    total_slots: int = 5


class Town(Settlement):
    total_slots: int = 3


class Province(BaseModel):
    fertility: int
    public_order: int
    city: City = Field(default_factory = lambda : City())
    town: list[Town] = Field(default_factory = lambda : [Town(), Town()])




