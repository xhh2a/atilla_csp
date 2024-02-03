from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    Modifier,
    ModifierType,
    UnitType,
    VariableType,
    ModifierLocation,
)


class GermanPortBuildings(Enum):
    TRADE_PORT = Building(
        name="Trade Port",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-6
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=2500
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=40),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=4),
        ],
        chain=BuildingChain.PORT,
        building_location=BuildingLocation.ANY,
    )
    FISHING_PORT = Building(
        name="Fishing Port",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-6
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1250
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=90),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=4),
        ],
        chain=BuildingChain.PORT,
        building_location=BuildingLocation.ANY,
    )
    MILITARY_PORT = Building(
        name="Military Port",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                sub_category=UnitType.NAVAL,
                value=2,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.UNIT_LEVEL,
                sub_category=UnitType.NAVAL,
                value=2,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=6),
        ],
        chain=BuildingChain.WATERWORKS,
        building_location=BuildingLocation.ANY,
    ),


BUILDING_CHAINS = [
    GermanPortBuildings.FISHING_PORT.value, GermanPortBuildings.TRADE_PORT.value
]
