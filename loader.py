from types import ModuleType
import data_classes

from importlib import import_module
from configuration import ContextVariableKeys, set_context, setup_context, get_context
from data_classes.cultures import CultureType
from data_classes.parameters import RequestParameter
from data_classes.province import Building, BuildingChain, BuildingLocation, Province
from data_classes.types import ReligionType


def load_data(request_parameters: RequestParameter):
    set_context(ContextVariableKeys.GAME, request_parameters.game)
    _load_data_module(request_parameters)
    _load_building_chains(request_parameters)


def _load_data_module(request_parameters: RequestParameter):
    data_module = import_module(
        f"data.{get_context(ContextVariableKeys.GAME)}.{request_parameters.culture.value}"
    )
    set_context(ContextVariableKeys.DATA_MODULE, data_module)


def _load_building_chains(request_parameters: RequestParameter) -> list[Building]:
    culture_buildings = get_context(ContextVariableKeys.DATA_MODULE).BUILDING_CHAINS
    all_buildings_available = [
        *culture_buildings,
        *request_parameters.primary_religion.building_chains,
        *(
            request_parameters.secondary_religion.building_chains
            if request_parameters.secondary_religion
            else []
        ),
    ]
    set_context(ContextVariableKeys.BUILDING_CHAINS, all_buildings_available)
    # Cache settlement building
    main_city_building = None
    city_buildings_options = set()
    main_town_building = None
    town_building_options = set()
    port_buildings = set()
    for building in all_buildings_available:
        building: Building = building
        match building.chain:
            case BuildingChain.CITY:
                main_city_building = building
            case BuildingChain.TOWN:
                main_town_building = building
            case BuildingChain.PORT:
                port_buildings.add(building)
            case _:
                if building.building_location in { BuildingLocation.CITY, BuildingLocation.ANY }:
                    city_buildings_options.add(building)
                elif building.building_location in { BuildingLocation.TOWN, BuildingLocation.ANY }:
                    town_building_options.add(building)

    set_context(ContextVariableKeys.CITY_BUILDING, main_city_building)
    set_context(ContextVariableKeys.TOWN_BUILDING, main_town_building)
    set_context(ContextVariableKeys.PORT_BUILDINGS, port_buildings)
    set_context(ContextVariableKeys.CITY_BUILDING_OPTIONS, city_buildings_options)
    set_context(ContextVariableKeys.TOWN_BUILDING_OPTIONS, town_building_options)


if __name__ == "__main__":
    setup_context()
    load_data(
        RequestParameter(
            province=Province(fertility=3, public_order=-9),
            game="atilla",
            culture=CultureType.DESERT_TRIBES,
            primary_religion_type=ReligionType.SEMETIC_PAGANISM,
        )
    )
