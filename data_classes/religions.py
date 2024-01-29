
from contextvars import ContextVar
from dataclasses import Field
from humps import pascalize

from pydantic import BaseModel
from configuration import ContextVariableKeys
from data_classes.province import Building

from data_classes.types import Edict, Modifier, ReligionType, Variable



class Religion(BaseModel):
    religion_type: ReligionType
    modifiers: list[Modifier]
    edicts: list[Edict]
    city_building_chain: list[Building] = Field(default_factory = lambda : [])
    town_building_chain: list[Building] = Field(default_factory = lambda : [])



def load_religion(religion_type: ReligionType) -> Religion:
    from importlib import import_module

    return import_module(f"data.{ContextVar(ContextVariableKeys.GAME).get()}.religions.{religion_type}.{pascalize(religion_type)}")

def _swap_faith(modifier):
    if modifier.variable == Variable.FAITH:
        modifier.variable = Variable.ALTERNATE_FAITH
    elif modifier.variable == Variable.ALTERNATE_FAITH:
        modifier.variable = Variable.FAITH

def swap_variable_type_for_secondary_religion(religion: Religion):
    """
    Swaps primary and secondary faith modifiers
    """
    for modifier in religion.modifiers:
        _swap_faith(modifier)
    for edict in religion.edicts:
        for modifier in edict.modifiers:
            _swap_faith(modifier)
    for building in religion.city_building_chain:
        for modifier in building.modifiers:
            _swap_faith(modifier)
    for building in religion.town_building_chain:
        for modifier in building.modifiers:
            _swap_faith(modifier)
