from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import Modifier, ModifierLocation, ModifierType, VariableType


class GermanProvinceBuildings(Enum):
    CITY = Building(
        name="Burg",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.GROWTH,
                value=2,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=2
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=300
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=2),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=4),
        ],
        chain=BuildingChain.CITY,
        building_location=BuildingLocation.CITY,
    )
    TOWN = Building(
        name="Torp",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=150
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=1),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=4),
        ],
        chain=BuildingChain.TOWN,
        building_location=BuildingLocation.TOWN,
    )


BUILDING_CHAINS = [
    building.value for building in GermanProvinceBuildings
]