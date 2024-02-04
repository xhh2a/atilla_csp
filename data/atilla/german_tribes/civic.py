from enum import Enum
from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.types import (
    AgentType,
    Modifier,
    ModifierType,
    UnitType,
    VariableType,
    ModifierLocation,
)


class GermanCivicBuildings(Enum):
    TRADE_MARKET = Building(
        name="Amber Market",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=2500
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.ROAD, value=30),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.SPY,
            ),
        ],
        chain=BuildingChain.TRADE_MARKET,
        building_location=BuildingLocation.CITY,
    )
    FOOD_MARKET = Building(
        name="Fairground",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=60),
            Modifier(type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1000),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.ALL_INCOME, value=0.1
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.SPY,
            ),
        ],
        chain=BuildingChain.FOOD_MARKET,
        building_location=BuildingLocation.CITY,
    )
    SLAVE_MARKET = Building(
        name="Slave Market",
        modifiers=[
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-4,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=-4
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.COMMERCE, value=1450
            ),
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
    )
    ACADEMY = Building(
        name="Hall of Elders",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-100),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.RESEARCH, value=0.15
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=9),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=825),
        ],
        chain=BuildingChain.RESEARCH,
        building_location=BuildingLocation.CITY,
    )
    CITY_CIVIC_CENTER = Building(
        name="Communal Grounds",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-100),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=13
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=825),
            Modifier(type=ModifierType.FLAT, variable=VariableType.UNIT_LEVEL, sub_category=UnitType.LAND, value=1),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.CHAMPION,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.CITY,
    )
    CITY_PUBLIC_ORDER = Building(
        name="Mead Hall",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-100),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.SANITATION,
                location=ModifierLocation.SETTLEMENT,
                value=-6,
            ),
            Modifier(
                type=ModifierType.PERCENTAGE,
                variable=VariableType.PUBLIC_ORDER,
                value=22,  # 5 from 30% immigration penalty
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.CULTURE, value=1650),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.CITY,
    )
    TOWN_CIVIC_CENTER = Building(
        name="Chieftain's Keep",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-100),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.PUBLIC_ORDER,
                value=13,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.CULTURE, value=825
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.UNIT_LEVEL, sub_category=UnitType.LAND, value=1),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.CHAMPION,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=1
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.TOWN,
    )
    TOWN_CAPITAL = Building(
        name="Chieftain's Castle",
        modifiers=[
            Modifier(type=ModifierType.FLAT, variable=VariableType.FOOD, value=-150),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.PUBLIC_ORDER,
                value=16,
            ),
            Modifier(
                type=ModifierType.FLAT, variable=VariableType.CULTURE, value=1500
            ),
            Modifier(type=ModifierType.FLAT, variable=VariableType.UNIT_LEVEL, sub_category=UnitType.LAND, value=2),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_ENABLE,
                value=AgentType.CHAMPION,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.AGENT_CAP,
                sub_category=AgentType.CHAMPION,
                value=1,
            ),
            Modifier(
                type=ModifierType.FLAT,
                variable=VariableType.RECRUITMENT_CAPACITY,
                value=2
            ),
        ],
        chain=BuildingChain.CIVIC_CENTER,
        building_location=BuildingLocation.TOWN,
    )

BUILDING_CHAINS = [
    building.value for building in GermanCivicBuildings
    if building not in [GermanCivicBuildings.TOWN_CAPITAL]
]
