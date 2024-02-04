from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.religions import Religion
from data_classes.types import (
    AgentType,
    ModifierLocation,
    Modifier,
    ModifierType,
    ReligionType,
    VariableType,
    Edict,
)


GermanicPaganism = Religion(
    religion_type=ReligionType.GERMANIC_PAGANISM,
    modifiers=[
        Modifier(
            type=ModifierType.FLAT,
            variable=VariableType.RECRUITMENT_CAPACITY,
            value=1,
        )
    ],
    edicts=[
    ],
    building_chains=[
        Building(
            name="Temple of Wodan",
            modifiers=[
                Modifier(
                    type=ModifierType.FLAT, variable=VariableType.FOOD, value=-80
                ),
                Modifier(
                    type=ModifierType.FLAT, variable=VariableType.PUBLIC_ORDER, value=5
                ),
                Modifier(type=ModifierType.FLAT, variable=VariableType.FAITH, value=10),
                Modifier(
                    type=ModifierType.FLAT,
                    variable=VariableType.AGENT_ENABLE,
                    value=AgentType.PRIEST,
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable=VariableType.AGENT_CAP,
                    sub_category=AgentType.PRIEST,
                    value=1,
                ),
            ],
            chain=BuildingChain.RELIGION_1,
            building_location=BuildingLocation.CITY,
        ),
        Building(
            name="Germanic Barrows",
            modifiers=[
                Modifier(type=ModifierType.FLAT, variable=VariableType.SANITATION, location=ModifierLocation.PROVINCE, value=3),
                Modifier(type=ModifierType.FLAT, variable=VariableType.FAITH, value=2),
                Modifier(type=ModifierType.FLAT, variable=VariableType.FAITH, location=ModifierLocation.ADJACENT, value=1),
            ],
            chain=BuildingChain.RELIGION_1,
            building_location=BuildingLocation.TOWN,
        ),
    ],
)
