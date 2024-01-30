from typing import Any
from configuration import ContextVariableKeys, get_context
import data_classes
from data_classes.parameters import RequestParameter
from collections import namedtuple
from data_classes.province import Province
from itertools import combinations
from funcy import group_by

import loader

from collections import deque


SearchSpace = namedtuple('SearchSpace', ['province'])
    
def _iterative_depth_first_search(request: RequestParameter, fringe: list[Province], current_element: Province, evaluated: list[Any]):
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
    else:
        city = province.city
        if not city.is_complete:
            possible_city_buildings = [building for building in [*get_context(ContextVariableKeys.CITY_BUILDING_OPTIONS), *city.trade_good_buildings] if building.chain not in city.existing_building_chains]
            desired_slots = city.total_slots - 1
            if city.has_port:
                desired_slots -= 1
            for combination in combinations(possible_city_buildings, desired_slots):
                if max(len(v) for v in group_by(lambda b: b.chain, combination).values()) > 1:
                    continue
                if city.has_port:
                    for port_building in get_context(ContextVariableKeys.PORT_BUILDINGS):
                        copy_province = province.model_copy(deep=True)
                        copy_province.city.buildings.append(port_building)
                        copy_province.city.buildings.extend(combination)
                        fringe.append(copy_province)
                else:
                    copy_province = province.model_copy(deep=True)
                    copy_province.city.buildings.extend(combination)
                    fringe.append(copy_province)
        else:
            towns = [(province.first_town, 'first_town'), (province.second_town, 'second_town')]
            for town, attribute in towns:
                if town.is_complete:
                    continue
                possible_town_buildings = [building for building in [*get_context(ContextVariableKeys.TOWN_BUILDING_OPTIONS), *town.trade_good_buildings] if building.chain not in town.existing_building_chains]
                desired_slots = town.total_slots - 1
                if town.has_port:
                    desired_slots -= 1
                for combination in combinations(possible_town_buildings, desired_slots):
                    if max(len(v) for v in group_by(lambda b: b.chain, combination).values()) > 1:
                        continue
                    if town.has_port:
                        for port_building in get_context(ContextVariableKeys.PORT_BUILDINGS):
                            copy_province = province.model_copy(deep=True)
                            getattr(copy_province, attribute).buildings.append(port_building)
                            getattr(copy_province, attribute).buildings.extend(combination)
                            fringe.append(copy_province)
                    else:
                        copy_province = province.model_copy(deep=True)
                        getattr(copy_province, attribute).buildings.extend(combination)
                        fringe.append(copy_province)

def depth_first_search(request, province_callback):
    loader.setup_context()

    loader.load_data(
        request
    )

    fringe = deque([])
    evaluated = []
    fringe.append(province_callback())
    while fringe:
        _iterative_depth_first_search(request, fringe, fringe.pop(), evaluated)
    print(request._best_result.json())
    print(request._best_score)
    return request._best_result

if __name__ == "__main__":
    from data.atilla.trade_resources import TradeResource
    from data_classes.cultures import CultureType
    from data_classes.types import ReligionType

    from data_classes.province import Town, City
    loader.setup_context()

    depth_first_search(
        RequestParameter(
            game="atilla",
            culture=CultureType.DESERT_TRIBES,
            primary_religion_type=ReligionType.SEMETIC_PAGANISM,
            public_order=-19,
            food=0,
            sanitation=2,
            corruption=0.25,
            tax_rate=1,
        ),
        province_callback = lambda : Province(
            fertility=0,
            city=City(),
            first_town=Town(trade_good_buildings=[TradeResource.GEMSTONES.value])
        )
    )
    

