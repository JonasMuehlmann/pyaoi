from typing import Collection, Any, Callable
from lib import libstd

UnaryPredicate = Callable[[Any], bool]
"""A function that takes one argument and returns a bool"""

def all_of(collection: Collection, unary_predicate: UnaryPredicate) -> bool:
    """Foo Bar 123"""
    return libstd.all_of_impl(collection, unary_predicate)