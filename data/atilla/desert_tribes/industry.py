from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    ModifierLocation,
    UnitType,
    VariableType,
    Modifier,
    ModifierType,
)


BUILDING_CHAINS = [
    Building(
        name="Builder's Workshop",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-10,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=1650
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.CONSTRUCTION_COST,
                value=-0.15,
            ),
        ],
        chain=BuildingChain.INDUSTRY_CONSTRUCTION,
        building_location=BuildingLocation.TOWN,
    ),
    Building(
        name="Carpet Maker",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-8,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-8
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=2500
            ),
        ],
        chain=BuildingChain.INDUSTRY_MONEY,
        building_location=BuildingLocation.TOWN,
    ),
    Building(
        name="Mosaic Workshop",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-10,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=2000
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.CULTURE, value=0.15
            ),
        ],
        chain=BuildingChain.INDUSTRY_CULTURE,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Adobe Kiln",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-10,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=1250
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1250
            ),
        ],
        chain=BuildingChain.INDUSTRY_CULTURE,
        building_location=BuildingLocation.CITY,
    ),
]
