from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    ModifierLocation,
    UnitType,
    VariableType,
    Modifier,
    ModifierType,
)


class GermanIndustryBuildings(Enum):
    CONSTRUCTION = Building(
        name="Plastermaker",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-8
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=1250
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.CONSTRUCTION_COST,
                value=-0.10,
            ),
        ],
        chain=BuildingChain.INDUSTRY_CONSTRUCTION,
        building_location=BuildingLocation.ANY,
    )
    MONEY = Building(
        name="Bone Crafters' Guild",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-8,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=2000
            ),
        ],
        chain=BuildingChain.INDUSTRY_MONEY,
        building_location=BuildingLocation.ANY,
    )
    COMMERCE = Building(
        name="Basket Weavers' Guild",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-8
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=1250
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.1
            ),
        ],
        chain=BuildingChain.INDUSTRY_COMMERCE,
        building_location=BuildingLocation.ANY,
    )
    RANGED = Building(
        name="Carpenters' Guild",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=900
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.UNIT_AMMO,
                sub_category=UnitType.RANGED,
                value=0.10,
            ),
        ],
        chain=BuildingChain.INDUSTRY_RANGED,
        building_location=BuildingLocation.ANY,
    )
    ARMOR = Building(
        name="Smiths' Guild",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-10
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=900
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.UNIT_ARMOR,
                sub_category=UnitType.LAND,
                value=0.10,
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.UNIT_DAMAGE,
                sub_category=UnitType.LAND,
                value=0.10,
            ),
        ],
        chain=BuildingChain.INDUSTRY_ARMOR,
        building_location=BuildingLocation.ANY,
    )

BUILDING_CHAINS = [
    GermanIndustryBuildings.COMMERCE.value, GermanIndustryBuildings.CONSTRUCTION.value, GermanIndustryBuildings.MONEY.value
]