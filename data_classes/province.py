from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

from data_classes.types import Modifier


class Building(BaseModel):
    name: str
    modifiers: list[Modifier] = Field(default_factory = lambda: [])
    chain: str


class Settlement(BaseModel):
    total_slots: int = 0
    has_port: Optional[bool] = False
    trade_good_building: Optional[Building] = None


class City(Settlement):
    total_slots: int = 5


class Town(Settlement):
    total_slots: int = 3


class Province(BaseModel):
    fertility: int
    public_order: int
    city: City = Field(default_factory = lambda : City())
    town: list[Town] = Field(default_factory = lambda : [Town(), Town()])



