from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import Modifier, ModifierType, VariableType


BUILDING_CHAINS = [
    Building(
        name="Small City",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-30),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-1
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=3
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=300
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=10),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=3),
        ],
        chain=BuildingChain.CITY,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Hamlet",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-10),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=150
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=3),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=3),
        ],
        chain=BuildingChain.TOWN,
        building_location=BuildingLocation.TOWN,
    ),
]
