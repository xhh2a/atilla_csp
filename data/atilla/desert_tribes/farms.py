from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import UnitType, VariableType, Modifier, ModifierType


BUILDING_CHAINS = [
    Building(
        name="Wheat Querns",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-5
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=40),
            Modifier(type=ModifierType.FERTILITY, variable=VariableType.FOOD, value=34),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=80),
            Modifier(
                type=ModifierType.FERTILITY, variable=VariableType.FARMING, value=80
            ),
        ],
        chain=BuildingChain.FARMING_1,
        building_location=BuildingLocation.ANY,
    ),
    Building(
        name="Camel Ranch",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-5
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=130),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=825),
        ],
        chain=BuildingChain.FARMING_2,
        building_location=BuildingLocation.ANY,
    ),
    Building(
        name="Nisean Stables",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-5
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=50),
            Modifier(type=ModifierType.FERTILITY, variable=VariableType.FOOD, value=10),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=650),
            Modifier(
                type=ModifierType.FERTILITY, variable=VariableType.FARMING, value=200
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.UNIT_SPEED,
                sub_category=UnitType.CAVALRY,
                value=0.15,
            ),
        ],
        chain=BuildingChain.FARMING_3,
        building_location=BuildingLocation.ANY,
    ),
    Building(
        name="Sheep Barn",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-5
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=50),
            Modifier(type=ModifierType.FERTILITY, variable=VariableType.FOOD, value=7),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FARMING, value=1250),
            Modifier(
                type=ModifierType.FERTILITY, variable=VariableType.FARMING, value=165
            ),
        ],
        chain=BuildingChain.FARMING_3,
        building_location=BuildingLocation.ANY,
    ),
]
