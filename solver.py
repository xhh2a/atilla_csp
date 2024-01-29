

from contextvars import ContextVar
from configuration import ContextVariableKeys
from data_classes.parameters import RequestParameter


def load_data(request_parameters: RequestParameter):
    ContextVar(ContextVariableKeys.GAME).set(request_parameters.game)