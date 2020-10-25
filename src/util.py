#!/bin/python
import ast
import inspect
from types import LambdaType
# Taken from https://stackoverflow.com/a/48233305
from typing import Callable, Any


def contains_explicit_return(function: Callable) -> bool:
    """
    Args:
        function: Any function

    Returns:
        True if the function has an explicit return statement, False otherwise
    """
    return any(
        isinstance(node, ast.Return)
        for node in ast.walk(ast.parse(inspect.getsource(function)))
    )


def is_lambda(obj: Any) -> bool:
    """
    Args:
        obj: An object, which will be checked for being a lambda

    Returns:
        True if obj is of type lambda, False otherwise
    """
    return isinstance(obj, LambdaType)
 