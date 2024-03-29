from typing import Any, Optional
from pydantic import BaseModel, Field
from data_classes.cultures import CultureType
from data_classes.province import Building, Province
from humps import pascalize
from data_classes.religions import (
    ReligionType,
    load_religion,
    swap_variable_type_for_secondary_religion,
)
from data_classes.types import Modifier


class RequestParameter(BaseModel):
    game: str
    culture: CultureType
    primary_religion_type: ReligionType
    _primary_religion: Any = None
    secondary_religion_type: Optional[ReligionType] = None
    _secondary_religion: Any = None
    food: int = 0
    public_order: int = 0
    sanitation: int = 0
    corruption: float = 0.5
    tax_rate: float = 1.0
    _best_score: float = 0.0
    _best_result: Any = None
    # faith_target: int = 0
    # alternate_faith_target: int = 0
    # current_corruption: float = 0.0
    existing_modifiers: list[Modifier] = Field(default_factory=lambda: [])
    additional_buildings: list[Building] = Field(default_factory=list)

    @property
    def primary_religion(self):
        if not self._primary_religion:
            self._primary_religion = load_religion(self.primary_religion_type)
        return self._primary_religion

    @property
    def secondary_religion(self):
        if self.secondary_religion_type and self._secondary_religion is None:
            self._secondary_religion = load_religion(self.secondary_religion_type)
            swap_variable_type_for_secondary_religion(self._secondary_religion)
        return self._secondary_religion
