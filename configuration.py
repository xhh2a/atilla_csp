from enum import Enum
import threading
from typing import Any


class Configuration(int, Enum):
    DIFFICULTY_PUBLIC_ORDER = -9


class ContextVariableKeys(str, Enum):
    GAME = "game"
    DATA_MODULE = "data_module"


def setup_context():
    global __context__
    __context__ = threading.local()

def set_context(context_key: ContextVariableKeys, value: Any):
    global __context__
    setattr(__context__, context_key, value)

def get_context(context_key: ContextVariableKeys, default: Any = None):
    global __context__
    return getattr(__context__, context_key, default)
