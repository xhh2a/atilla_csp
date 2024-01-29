from data_classes.province import Building, BuildingChain
from data_classes.religions import Religion
from data_classes.types import AgentType, Location, Modifier, ModifierType, ReligionType, Variable, Edict


SemeticPaganism = Religion(
    religion_type=ReligionType.SEMETIC_PAGANISM,
    modifiers=[
        Modifier(
            type=ModifierType.PERCENTAGE,
            variable=Variable.REPLENISHMENT,
            value=0.05,
        )
    ],
    edicts=[
        Edict(
            name="Trade and Industry",
            modifiers=[
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = Variable.INDUSTRY,
                    value = 0.1,
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = Variable.COMMERCE,
                    value = 0.1,
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FAITH,
                    value = -3
                )
            ],
        ),
        Edict(
            name="Military Fervour",
            modifiers=[
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = Variable.RECRUITMENT_CAPACITY,
                    value = 1
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = Variable.REPLENISHMENT,
                    value = 0.03
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FAITH,
                    value = 3
                )
            ],
        )
    ],
    city_building_chain=[
        Building(
            name="Enclosure of Almaqah",
            modifiers=[
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FOOD,
                    value = -125
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.PUBLIC_ORDER,
                    value = 10
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FAITH,
                    value = 10
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FAITH,
                    location = Location.ADJACENT,
                    value = 1
                ),
                Modifier(
                    type=ModifierType.PERCENTAGE,
                    variable = Variable.FARMING,
                    value = 1
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.AGENT_ENABLE,
                    value = AgentType.PRIEST
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.AGENT_CAP,
                    sub_category = AgentType.PRIEST,
                    value = 1
                ),
            ],
            chain=BuildingChain.CITY_RELIGION
        )
    ],
    town_building_chain=[
        Building(
            name="Large Stelae Field",
            modifiers=[
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.PUBLIC_ORDER,
                    value = 6
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FOOD,
                    value = 30
                ),
                Modifier(
                    type=ModifierType.FLAT,
                    variable = Variable.FAITH,
                    value = 7
                ),
            ],
            chain=BuildingChain.TOWN_RELIGION,
        )
    ],
)
