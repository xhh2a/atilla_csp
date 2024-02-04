from pkgutil import walk_packages
from pathlib import Path
from importlib import import_module
from funcy import flatten

packages = list(
    walk_packages([Path(__file__).parent.absolute().as_posix()], prefix=__name__ + ".")
)

BUILDING_CHAINS = list(
    flatten(
        [
            import_module(file.name).BUILDING_CHAINS
            for file in packages
            if file.name != "__init__.py"
        ]
    )
)