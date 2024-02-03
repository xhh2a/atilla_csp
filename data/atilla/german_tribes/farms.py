from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    ModifierLocation,
    UnitType,
    VariableType,
    Modifier,
    ModifierType,
)


class GermanFarmBuildings(Enum):
    CATTLE_FARM = Building(
        name="Livestock Pens",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=40),
            Modifier(type=ModifierType.FERTILITY, variable=VariableType.FOOD, value=10),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=500),
            Modifier(
                type=ModifierType.FERTILITY, variable=VariableType.FARMING, value=150
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.UNIT_SPEED,
                sub_category=UnitType.CAVALRY,
                value=0.10,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
        ],
        chain=BuildingChain.FARMING_STABLES,
        building_location=BuildingLocation.TOWN,
    )
    GOAT_FARM = Building(
        name="Goat Barns",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-4
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=70),
            Modifier(type=ModifierType.FERTILITY, variable=VariableType.FOOD, value=12),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=450),
            Modifier(
                type=ModifierType.FERTILITY, variable=VariableType.FARMING, value=75
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
        ],
        chain=BuildingChain.FARMING_SHEEP,
        building_location=BuildingLocation.TOWN,
    )


BUILDING_CHAINS = [
    building.value for building in GermanFarmBuildings
]
