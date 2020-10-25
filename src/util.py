#!/bin/python


#  This file is part of python_std_algorithm.
#  Copyright (C) 2020 Jonas Muehlmann
# 
#      python_std_algorithm is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
# 
#      python_std_algorithm is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
# 
#      You should have received a copy of the GNU General Public License
#      along with python_std_algorithm.  If not, see <https://www.gnu.org/licenses/>.

import ast
import inspect
from types import LambdaType

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
