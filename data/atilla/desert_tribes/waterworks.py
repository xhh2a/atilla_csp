from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import Modifier, ModifierType, VariableType, ModifierLocation


BUILDING_CHAINS = [
    Building(
        name="Yakhchal",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=9,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=90),
        ],
        chain=BuildingChain.WATERWORKS,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Royal Hamam",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-80),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                value=6,
                location=ModifierLocation.SETTLEMENT,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.PROVINCE,
                value=7,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=7
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=1250),
        ],
        chain=BuildingChain.WATERWORKS,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Fountains",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=-150
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                value=6,
                location=ModifierLocation.SETTLEMENT,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.PROVINCE,
                value=7,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=4
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GROWTH, value=9),
        ],
        chain=BuildingChain.WATERWORKS,
        building_location=BuildingLocation.TOWN,
    ),
]
