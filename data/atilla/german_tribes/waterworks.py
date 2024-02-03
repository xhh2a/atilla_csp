from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import Modifier, ModifierType, VariableType, ModifierLocation


class GermanicWaterworks(Enum):
    CITY_RESERVES = Building(
        name="Smokehouse",
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
    )
    TOWN_WATERWORKS = Building(
        name="Canals",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                value=5,
                location=ModifierLocation.SETTLEMENT,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.PROVINCE,
                value=4,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GROWTH, value=9),
        ],
        chain=BuildingChain.WATERWORKS,
        building_location=BuildingLocation.TOWN,
    )

BUILDING_CHAINS = [
    building.value for building in GermanicWaterworks
]

