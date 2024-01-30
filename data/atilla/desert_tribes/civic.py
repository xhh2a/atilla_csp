from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    AgentType,
    Modifier,
    ModifierType,
    VariableType,
    ModifierLocation,
)


BUILDING_CHAINS = [
    Building(
        name="Oriental Market",
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
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=2000
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=25),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.15
            ),
        ],
        chain=BuildingChain.TRADE_MARKET,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Food Market",
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
            Modifier(type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=400),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=20),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.FARMING, value=0.15
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.SPY,
            ),
        ],
        chain=BuildingChain.FOOD_MARKET,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Slave Market",
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
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1450
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=20),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.15
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.SPY,
            ),
        ],
        chain=BuildingChain.SLAVE_MARKET,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Academy",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-80),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.RESEARCH, value=0.2
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=1250),
        ],
        chain=BuildingChain.RESEARCH,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Imperial Gardens",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-40),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=13
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=500),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.AGENT_LEVEL, value=2
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Grand Palace",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-80),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=13
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=1200),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.TAX_RATE, value=0.1
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.CHAMPION,
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Majore Field",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-100),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.PUBLIC_ORDER,
                value=21,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=825),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.CITY,
    ),
    Building(
        name="Caravanserai",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-40),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.PUBLIC_ORDER,
                value=-4,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1250
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.TRADE_INCOME,
                value=0.03,
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=0.2),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.TOWN,
    ),
    Building(
        name="Governor's Palace",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-40),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.PUBLIC_ORDER,
                value=-9,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.TAX_RATE, value=0.06
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.TOWN,
    ),
]
