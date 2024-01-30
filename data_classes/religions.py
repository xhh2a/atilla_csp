from contextvars import ContextVar
from humps import pascalize

from pydantic import BaseModel, Field
from configuration import ContextVariableKeys, get_context
from data_classes.province import Building

from data_classes.types import Edict, Modifier, ReligionType, VariableType


class Religion(BaseModel):
    religion_type: ReligionType
    modifiers: list[Modifier]
    edicts: list[Edict]
    building_chains: list[Building] = Field(default_factory=list)


def load_religion(religion_type: ReligionType) -> Religion:
    from importlib import import_module

    return getattr(
        import_module(
            f"data.{get_context(ContextVariableKeys.GAME)}.religions.{religion_type.value}"
        ),
        pascalize(religion_type.value),
    )


def _swap_faith(modifier):
    if modifier.variable == VariableType.FAITH:
        modifier.variable = VariableType.ALTERNATE_FAITH
    elif modifier.variable == VariableType.ALTERNATE_FAITH:
        modifier.variable = VariableType.FAITH


def swap_variable_type_for_secondary_religion(religion: Religion):
    """
    Swaps primary and secondary faith modifiers
    """
    for modifier in religion.modifiers:
        _swap_faith(modifier)
    for edict in religion.edicts:
        for modifier in edict.modifiers:
            _swap_faith(modifier)
    for building in religion.building_chains:
        for modifier in building.modifiers:
            _swap_faith(modifier)
