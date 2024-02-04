from data.atilla.german_tribes.civic import GermanCivicBuildings
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

    frank_faction = RequestParameter(
        game="atilla",
        culture=CultureType.GERMAN_TRIBES,
        primary_religion_type=ReligionType.GERMANIC_PAGANISM,
        public_order=-21,
        food=0,
        sanitation=2,
        corruption=0.25,
        tax_rate=1,
    )

    searches = []

    # Frisia
    searches.append(
        dict(
            request=frank_faction,
            province_args=dict(
                fertility=0,
                city=dict(
                    trade_good_buildings=[
                        TradeResource.FUR.value,
                    ]
                ),
                first_town=dict(
                    has_port=True,
                    buildings=[
                        GermanCivicBuildings.TOWN_CAPITAL.value,
                    ],
                ),
                second_town=dict(),
            ),
            output_location=Path("./results/atilla/franks/frisia.json"),
        )
    )

    # Belgica
    searches.append(dict(
        request=frank_faction,
        province_args=dict(
            fertility=0,
            city=dict(
                trade_good_buildings=[TradeResource.TIMBER.value]
            ),
            first_town=dict(),
            second_town=dict(),
        ),
        output_location=Path("./results/atilla/franks/belgica.json"),
    ))

    # North Burgundy Maxima Sequanorum
    searches.append(dict(
        request=frank_faction,
        province_args=dict(
            fertility=0,
            city=dict(),
            first_town=dict(
                trade_good_buildings=[TradeResource.IRON_MONEY.value]
            ),
            second_town=dict(),
        ),
        output_location=Path("./results/atilla/franks/maxima_sequanorum.json"),
    ))

    #Scandza
    searches.append(dict(
        request=frank_faction,
        province_args=dict(
            fertility=0,
            city=dict(
                has_port=True,
                trade_good_buildings=[TradeResource.TIMBER.value]
                ),
            first_town=dict(
                has_port=True,
                
            ),
            second_town=dict(
                has_port=True,
            ),
        ),
        output_location=Path("./results/atilla/franks/scandza.json"),
    ))

    def parallelism(search_arguments):
        return depth_first_search(**search_arguments)

    with Pool(cpu_count()) as executor:
        print(f"Running over {cpu_count()} threads")
        print(executor.map(parallelism, searches))
