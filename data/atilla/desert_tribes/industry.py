from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    ModifierLocation,
    UnitType,
    VariableType,
    Modifier,
    ModifierType,
)

class DesertIndustryBuildings(Enum):
    CONSTRUCTION = Building(
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
    )
    MONEY = Building(
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
    )
    CULTURE = Building(
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
    )
    COMMERCE = Building(
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
        chain=BuildingChain.INDUSTRY_COMMERCE,
        building_location=BuildingLocation.CITY,
    )
    PLEASURE = Building(
        name="1000 Pleasures",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-12,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=4
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=3500
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.FAITH, value=-13
            ),
        ],
        chain=BuildingChain.INDUSTRY_PLEASURE,
        building_location=BuildingLocation.CITY,
    )


BUILDING_CHAINS = [
    building.value for building in DesertIndustryBuildings
    if building not in [DesertIndustryBuildings.PLEASURE]
]