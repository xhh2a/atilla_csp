from data.atilla.desert_tribes.civic import DesertCivicBuildings
from data.atilla.desert_tribes.industry import DesertIndustryBuildings
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

    aksum_faction = RequestParameter(
        game="atilla",
        culture=CultureType.DESERT_TRIBES,
        primary_religion_type=ReligionType.SEMETIC_PAGANISM,
        # secondary_religion_type=ReligionType.EASTERN_CHRISTIANITY,
        additional_buildings=[DesertIndustryBuildings.PLEASURE.value],
        public_order=-21,
        food=0,
        sanitation=2,
        corruption=0.25,
        tax_rate=1,
    )

    searches = []

    # Aethiopia
    searches.append(
        dict(
            request=aksum_faction,
            province_args=dict(
                fertility=0,
                city=dict(
                    buildings=[
                        DesertCivicBuildings.CITY_CAPITAL.value,
                        DesertCivicBuildings.AKSUM_MARKET.value,
                    ],
                    trade_good_buildings=[TradeResource.FUR.value],
                ),
                first_town=dict(
                    buildings=[
                        TradeResource.SPICES.value,
                    ],
                ),
                second_town=dict(),
            ),
            output_location=Path("./results/atilla/aksum/aethiopia.json"),
        )
    )

    # Arabia Felix
    # searches.append(dict(
    #     request=aksum_faction,
    #     province_args=dict(
    #         fertility=0,
    #         city=dict(
    #             trade_good_buildings=[TradeResource.TIMBER.value]
    #         ),
    #         first_town=dict(),
    #         second_town=dict(),
    #     ),
    #     output_location=Path("./results/atilla/aksum/arabia_felix.json"),
    # ))

    def parallelism(search_arguments):
        return depth_first_search(**search_arguments)

    with Pool(cpu_count()) as executor:
        print(f"Running over {cpu_count()} threads")
        print(executor.map(parallelism, searches))
