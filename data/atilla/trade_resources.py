from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    ModifierLocation,
    UnitType,
    VariableType,
    Modifier,
    ModifierType,
)


class TradeResource(Enum):
    GEMSTONES = Building(
        name="Gem Market",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 20,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    DYES = Building(
        name="Dye Factory",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.08
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.08
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 12,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    OLIVE_OIL = Building(
        name="Olive Oil Mill",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-5,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=170),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.2
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 6
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    MARBLE_CULTURE = Building(
        name="Sculptor",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FAITH, value=3),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.CULTURE, value=0.2
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.CONSTRUCTION_COST,
                value=-0.15,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=20 * 8
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    MARBLE_INDUSTRY = Building(
        name="Marble Quarry Complex",
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
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=1650
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 8
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    GOLD_COMMERCE = Building(
        name="Jeweller",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-10,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-15
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=3000
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.TRADE_INCOME,
                value=0.15,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    GOLD_INDUSTRY = Building(
        name="Deep Gold Mine",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-10,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-15
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=2500
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    LEAD = Building(
        name="Deep Gold Mine",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.2
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 5
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    TIMBER = Building(
        name="Lumbar Camp",
        modifiers=[
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.2
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 5
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    IRON_MONEY = Building(
        name="Foundry",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.15
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.FARMING, value=0.15
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 6
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    FRUIT_FOOD = Building(
        name="Fruit Dryer",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-5,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=5
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=170),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=20 * 10
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    FRUIT_INCOME = Building(
        name="Winery",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-5,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=9
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=90),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 10,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    SALT = Building(
        name="Salt Trading Post",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=90),
            Modifier(type=ModifierType.FLAT, variable=VariableType.INDUSTRY, value=900),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=160 * 8
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    SPICES = Building(
        name="Spice Trading Port",
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
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=35),
            Modifier(type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=825),
            Modifier(type=ModifierType.FLAT, variable=VariableType.GARRISON, value=4),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 14,
            ),
        ],
        chain=BuildingChain.PORT,
    )
    FUR = Building(
        name="Fur Market",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-5,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=90),
            Modifier(type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=500),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 10,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
    SILK = Building(
        name="Fur Market",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=35),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.2
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SUBSISTENCE,
                value=160 * 16,
            ),
        ],
        chain=BuildingChain.TRADE_RESOURCE,
    )
