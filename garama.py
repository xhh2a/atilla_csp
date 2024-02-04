from data.atilla.desert_tribes.civic import DesertCivicBuildings
from data.atilla.trade_resources import TradeResource
from data_classes.cultures import CultureType
from data_classes.types import ReligionType

from data_classes.province import Town, City

from pathlib import Path
from typing import Any
from configuration import ContextVariableKeys, get_context
import data_classes
from data_classes.parameters import RequestParameter
from collections import namedtuple
from data_classes.province import Building, BuildingChain, BuildingLocation, Province
from itertools import combinations
from funcy import group_by
from data_classes.types import AgentType, Modifier, ModifierLocation, ModifierType, VariableType

import loader

from collections import deque

from concurrent.futures import ALL_COMPLETED, ProcessPoolExecutor, wait
from multiprocessing import Pool, cpu_count

from search import depth_first_search

if __name__ == "__main__":
    loader.setup_context()

    garama_faction = RequestParameter(
        game="atilla",
        culture=CultureType.DESERT_TRIBES,
        primary_religion_type=ReligionType.SEMETIC_PAGANISM,
        public_order=-19,
        food=0,
        sanitation=2,
        corruption=0.25,
        tax_rate=1,
    )

    garama_with_edict = RequestParameter(
        game="atilla",
        culture=CultureType.DESERT_TRIBES,
        primary_religion_type=ReligionType.SEMETIC_PAGANISM,
        public_order=-19,
        food=0,
        sanitation=2,
        corruption=0.35,
        tax_rate=1,
        existing_modifiers=[
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.COMMERCE, value=0.1
            ),
            Modifier(
                type=ModifierType.PERCENTAGE, variable=VariableType.INDUSTRY, value=0.1
            ),
        ],
    )
    
    searches = []

    # Lusitania
    searches.append(
        dict(
            request=garama_with_edict,
            province_args=dict(
                fertility=2,
                city=dict(),
                first_town=dict(
                    buildings=[
                        Building(
                            name="Military Port",
                            modifiers=[
                                Modifier(type=ModifierType.FLAT, variable=VariableType.SANITATION, value=-2)
                            ],
                            chain=BuildingChain.PORT,
                            building_location=BuildingLocation.ANY,
                        ),
                    ],
                ),
                second_town=dict(
                    buildings=[
                        TradeResource.IRON_MONEY.value,
                    ]
                ),
            ),
            output_location=Path("./results/garama/lusitania.json"),
        )
    )

    # Sahara
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=0,
            city=dict(
                buildings=[
                    DesertCivicBuildings.CITY_CAPITAL.value,
                ],
            ),
            first_town=dict(trade_good_buildings=[TradeResource.GEMSTONES.value]),
        ),
        output_location=Path("./results/garama/sahara.json"),
    ))

    # Mauretania
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=2,
            city=dict(has_port=True),
            first_town=dict(
                has_port=True,
                buildings=[TradeResource.TIMBER.value]
            ),
            second_town=dict(has_port=True),
        ),
        output_location=Path("./results/garama/mauretania.json"),
    ))

    # Carthage
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=2,
            city=dict(has_port=True),
            first_town=dict(
                trade_good_buildings=[
                    TradeResource.MARBLE_CULTURE.value,
                    TradeResource.MARBLE_INDUSTRY.value,
                ]
            ),
            second_town=dict(has_port=True),
        ),
        output_location=Path("./results/garama/carthage.json"),
    ))

    

    # Tripolitana
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=0,
            city=dict(has_port=True),
            first_town=dict(
                has_port=True, trade_good_buildings=[TradeResource.DYES.value]
            ),
            second_town=dict(has_port=True),
        ),
        output_location=Path("./results/garama/tripolitana.json"),
    ))

    # Libya
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=0,
            city=dict(
                has_port=True, trade_good_buildings=[TradeResource.OLIVE_OIL.value]
            ),
            first_town=dict(has_port=True),
            second_town=dict(),
        ),
        output_location=Path("./results/garama/libya.json"),
    ))

    # Egypt
    searches.append(dict(
        request=garama_with_edict,
        province_args=dict(
            fertility=2,
            city=dict(has_port=True),
            first_town=dict(has_port=True),
            second_town=dict(
                trade_good_buildings=[
                    TradeResource.GOLD_COMMERCE.value,
                    TradeResource.GOLD_INDUSTRY.value,
                ]
            ),
        ),
        output_location=Path("./results/garama/egypt.json"),
    ))

    # Baetica
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=1,
            city=dict(
                buildings=[
                    Building(
                        name="Cloca",
                        modifiers=[
                            Modifier(type=ModifierType.FLAT, variable=VariableType.SUBSISTENCE, value=-200),
                            Modifier(type=ModifierType.FLAT, variable=VariableType.SANITATION, location=ModifierLocation.SETTLEMENT, value=12),
                            Modifier(type=ModifierType.FLAT, variable=VariableType.SANITATION, location=ModifierLocation.PROVINCE, value=6),
                            Modifier(type=ModifierType.FLAT, variable=VariableType.GROWTH, value=13),
                        ],
                        chain=BuildingChain.WATERWORKS,
                        building_location=BuildingLocation.CITY,
                    ),
                ],
            ),
            first_town=dict(),
            second_town=dict(
                has_port=True,
                trade_good_buildings=[
                    TradeResource.FRUIT_INCOME.value,
                    TradeResource.FRUIT_FOOD.value,
                ]
            ),
        ),
        output_location=Path("./results/garama/baetica.json"),
    ))

    # Carthagenesis
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=1,
            city=dict(has_port=True),
            first_town=dict(),
            second_town=dict(
                trade_good_buildings=[
                    TradeResource.OLIVE_OIL.value,
                ]
            ),
        ),
        output_location=Path("./results/garama/carthagenesis.json"),
    ))

    # Terraconesis
    searches.append(dict(
        request=garama_faction,
        province_args=dict(
            fertility=0,
            city=dict(has_port=True),
            first_town=dict(),
            second_town=dict(
                trade_good_buildings=[
                    TradeResource.MARBLE_CULTURE.value,
                    TradeResource.MARBLE_INDUSTRY.value,
                ]
            ),
        ),
        output_location=Path("./results/garama/terraconesis.json"),
    ))

    def parallelism(search_arguments):
        return depth_first_search(**search_arguments)

    with Pool(cpu_count()) as executor:
        print(f"Running over {cpu_count()} threads")
        print(executor.map(parallelism, searches))
