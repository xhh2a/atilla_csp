import arrow

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


SearchSpace = namedtuple("SearchSpace", ["province"])


def _iterative_depth_first_search(
    request: RequestParameter,
    fringe: list[Province],
    current_element: Province,
    evaluated: list[Any],
    name: str
):
    province: Province = current_element
    if province.is_complete:
        resource_missing = province.get_missing_resource(
            current_public_order=request.public_order,
            current_food=request.food,
            current_sanitation=request.sanitation,
        )
        if resource_missing:
            return
        value = province.get_province_value(
            corruption=request.corruption,
            tax_rate=request.tax_rate,
        )
        if value > request._best_score:
            request._best_score = value
            request._best_result = province
            city_buildings = [
                building.name for building in request._best_result.city.buildings
            ]
            first_town = [
                building.name for building in request._best_result.first_town.buildings
            ]
            second_town = [
                building.name for building in request._best_result.second_town.buildings
            ]
            print(
                f"Found new Result for {name} Score: {value}\n{city_buildings}\n{first_town}\n{second_town}"
            )
            evaluated.append(f"Result for {name} Score: {value}\n{city_buildings}\n{first_town}\n{second_town}")
    else:
        city = province.city
        if not city.is_complete:
            possible_city_buildings = [
                building
                for building in [
                    *get_context(ContextVariableKeys.CITY_BUILDING_OPTIONS),
                    *city.trade_good_buildings,
                ]
                if building.chain not in city.existing_building_chains
            ]
            desired_slots = city.free_slots
            if city.has_port:
                desired_slots -= 1
            for combination in combinations(possible_city_buildings, desired_slots):
                if (
                    max(
                        len(v)
                        for v in group_by(lambda b: b.chain, combination).values()
                    )
                    > 1
                ):
                    continue
                if city.has_port:
                    for port_building in get_context(
                        ContextVariableKeys.PORT_BUILDINGS
                    ):
                        copy_province = province.model_copy(deep=True)
                        copy_province.city.buildings.append(port_building)
                        copy_province.city.buildings.extend(combination)
                        fringe.append(copy_province)
                else:
                    copy_province = province.model_copy(deep=True)
                    copy_province.city.buildings.extend(combination)
                    fringe.append(copy_province)
        else:
            towns = [
                (province.first_town, "first_town"),
                (province.second_town, "second_town"),
            ]
            for town, attribute in towns:
                if town.is_complete:
                    continue
                possible_town_buildings = [
                    building
                    for building in [
                        *get_context(ContextVariableKeys.TOWN_BUILDING_OPTIONS),
                        *town.trade_good_buildings,
                    ]
                    if building.chain not in town.existing_building_chains
                ]
                desired_slots = town.free_slots
                if town.has_port:
                    desired_slots -= 1
                for combination in combinations(possible_town_buildings, desired_slots):
                    if (
                        max(
                            len(v)
                            for v in group_by(lambda b: b.chain, combination).values()
                        )
                        > 1
                    ):
                        continue
                    if town.has_port:
                        for port_building in get_context(
                            ContextVariableKeys.PORT_BUILDINGS
                        ):
                            copy_province = province.model_copy(deep=True)
                            getattr(copy_province, attribute).buildings.append(
                                port_building
                            )
                            getattr(copy_province, attribute).buildings.extend(
                                combination
                            )
                            fringe.append(copy_province)
                    else:
                        copy_province = province.model_copy(deep=True)
                        getattr(copy_province, attribute).buildings.extend(combination)
                        fringe.append(copy_province)


def depth_first_search(request, province_args, output_location: Path = None):
    print(f"Starting Search for {output_location} {province_args}")
    if output_location is not None and output_location.exists():
        print(f"Cached results already exist for {output_location}, delete the file if you want to rerun")
        return
    start_time = arrow.now()
    # TODO: Use a priority queue multiple workers and greedy algorithm
    loader.setup_context()

    loader.load_data(request)
    request._best_result = None
    request._best_score = 0.0

    fringe = deque([])
    evaluated = []
    fringe.append(Province(**province_args))
    while fringe:
        _iterative_depth_first_search(request, fringe, fringe.pop(), evaluated, output_location)
    end_time = arrow.now()
    print(f"Completed Search in {end_time - start_time} {start_time.humanize()} for {output_location}")
    print(f"Writing results to {output_location}")
    print(request._best_result.json())
    print(request._best_score)
    if output_location is not None:
        Path(output_location).open("w").write(request._best_result.model_dump_json(indent=4))
        Path(Path(output_location).parent / output_location.name.replace(".json", "_log.txt")).open('w').write("\n".join(evaluated))
    return request._best_result

