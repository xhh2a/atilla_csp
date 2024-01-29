from data_classes.province import Building, BuildingChain, BuildingLocation
from data_classes.religions import Religion
from data_classes.types import AgentType, ModifierLocation, Modifier, ModifierType, ReligionType, VariableType, Edict


SemeticPaganism = Religion(
    religion_type=ReligionType.SEMETIC_PAGANISM,
    modifiers=[
        Modifier(
            type=ModifierType.PERCENTAGE,
            variable=VariableType.REPLENISHMENT,
            value=0.05,
        )
    ],
    edicts=[
        Edict(
            name="Trade and Industry",
            modifiers=[
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = VariableType.INDUSTRY,
                    value = 0.1,
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = VariableType.COMMERCE,
                    value = 0.1,
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FAITH,
                    value = -3
                )
            ],
        ),
        Edict(
            name="Military Fervour",
            modifiers=[
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = VariableType.RECRUITMENT_CAPACITY,
                    value = 1
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = VariableType.REPLENISHMENT,
                    value = 0.03
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FAITH,
                    value = 3
                )
            ],
        )
    ],
    building_chains=[
        Building(
            name="Enclosure of Almaqah",
            modifiers=[
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FOOD,
                    value = -125
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.PUBLIC_ORDER,
                    value = 10
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FAITH,
                    value = 10
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FAITH,
                    location = ModifierLocation.ADJACENT,
                    value = 1
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = VariableType.FARMING,
                    value = 0.4
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.AGENT_ENABLE,
                    value = AgentType.PRIEST
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.AGENT_CAP,
                    sub_category = AgentType.PRIEST,
                    value = 1
                ),
            ],
            chain=BuildingChain.RELIGION_1,
            building_location=BuildingLocation.CITY
        ),
        Building(
            name="Large Stelae Field",
            modifiers=[
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.PUBLIC_ORDER,
                    value = 6
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FOOD,
                    value = 30
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = VariableType.FAITH,
                    value = 7
                ),
            ],
            chain=BuildingChain.RELIGION_1,
            building_location=BuildingLocation.TOWN
        )
    ],
)
