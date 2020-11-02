"""A pure python implementation of the C++ Standard Template Library(STL)'s algorithm header"""
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

#!/usr/bin/env python3
import itertools
import operator
from typing import (
    Callable,
    Any,
    Tuple,
    Optional,
    Iterable,
    MutableSequence,
    Collection,
    Sequence,
)

UnaryPredicate = Callable[[Any], bool]
"""A callable that takes one argument and returns a bool"""
BinaryPredicate = Callable[[Any, Any], bool]
"""A callable that takes two arguments and returns a bool"""

UnaryFunction = Callable[[Any], None]
"""A callable that takes one argument and returns none"""


def all_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """
    Check if an unary predicate returns True for all elements in the iterable, or if the iterable is empty

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for every element in the iterable, or the iterable is empty, False otherwise
    """
    return all(map(unary_predicate, iterable))


def any_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """
    Check if an unary predicate returns True for any elements in the iterable, or if the iterable is empty

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for any element in the iterable, False otherwise or when the iterable is empty
    """
    return any(map(unary_predicate, iterable))


def none_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """
    Check if an unary predicate returns False for any elements in the iterable, or if the iterable is empty

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to False for every element in the iterable, False otherwise or when the iterable is empty
    """
    return True if not iterable else not all(map(unary_predicate, iterable))


def for_each(
    mutable_sequence: MutableSequence,
    unary_function: UnaryFunction,
    readonly: bool = True,
) -> None:
    """
    Apply an unary function to each element in the mutable_sequence, modifying the elements

    Args:
        mutable_sequence: A mutable iterable to apply the unary_function to
        unary_function: An unary function to apply to each element in the mutable_sequence
        readonly: indicates whether the mutable_sequence is intended to be read or modified,defaults to True
    """
    if readonly:
        for element in mutable_sequence:
            unary_function(element)
    else:
        mutable_sequence[:] = list(map(unary_function, mutable_sequence))


def for_each_n(
    mutable_sequence: MutableSequence,
    unary_function: UnaryFunction,
    n: int,
    readonly: bool = True,
) -> None:
    """
    Apply an unary function to the first n elements in the mutable_sequence, modifying the elements

    Args:
        mutable_sequence: A mutable iterable to apply the unary_function to
        unary_function: An unary function to apply to each element in the mutable_sequence
        n: A number indicating the number of elements (counted from the start) to apply the unary_function to
        readonly: indicates whether the mutable_sequence is intended to be read or modified,defaults to True
    """
    if readonly:
        for element in mutable_sequence[:n]:
            unary_function(element)
    else:
        mutable_sequence[:n] = list(map(unary_function, mutable_sequence[:n]))


# CHECK: If using collections.Counter is faster
def count(sequence: Sequence, target: Any) -> int:
    """
    Count how often target appears in sequence

    Args:
        sequence: An iterable in which occurrences of target are counted
        target: A value/object, which's occurrences will be counted

    Returns:
        How often target appeared in sequence
    """
    return sequence.count(target)


def count_if(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """
    Count for how many elements in a iterable an unary predicate returns True

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns True
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns True

    Returns:
        For how many items unary predicate returned True
    """
    return sum(map(unary_predicate, iterable))
    # return reduce(lambda x, y: x + unary_predicate(y), iterable, 0)


def count_if_not(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """
    Count for how many elements in a iterable an unary predicate returns False

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns False
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns False

    Returns:
        For how many items unary predicate returned False, -1 if the iterable is empty
    """
    return -1 if not iterable else sum(map(lambda element: not unary_predicate(element), iterable))


def mismatch(
    iterable1: Iterable,
    iterable2: Iterable,
    binary_predicate: BinaryPredicate = operator.__eq__,
) -> Optional[Tuple[Any, Any]]:
    """
    Find the first pair of elements from both iterables, that are considered not equal
    Only indices until the last one of the shortest iterable are compared

    Args:
        iterable1: First iterable to use for comparison
        iterable2: Second iterable to use for comparison
        binary_predicate: A binary predicate, that returns true if the elements from both iterables are considered equal
            If not provided, operator.__eq__ will be used as a binary_predicate

    Returns:
        None, if one or more iterables is empty, or they do not differ until the end of the shortest iterable.
            If one indice has elements that are not considered equal, a Tuple of those elements will be returned

    Example:
        mismatch([], []) returns None since both iterables are empty

        mismatch([1, 2, 3, 4, 5], []) returns None, since one iterable is empty

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) returns None, since both iterables are considered equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) returns (5, 6), since  their fifth indice is considered not equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7, 8, 9]) returns (5, 6), since  their fifth indice is considered not equal.
        Since one iterable is longer, it's additional elements are not compared
    """
    if not iterable1 or not iterable2:
        return None
    # Since this library implements a function named min, the builtin has to be accesses through another name
    builtin_min: Callable = __builtins__["min"]
    last_index_shortest_iterable: int = builtin_min(len(iterable1), len(iterable2)) - 1

    return next(
        (pair for pair in zip(iterable1, iterable2) if not binary_predicate(*pair)),
        (
            iterable1[last_index_shortest_iterable],
            iterable2[last_index_shortest_iterable],
        ),
    )


def find(collection: Collection, target_element: Any) -> int:
    """
        Find the index of the first occurrence of target_element in collection
    Args:
        collection: A collection which to search through
        target_element: An element to search in the collection

    Returns:
        The index of target_element's first occurrence, -1 if it was not found
    """
    try:
        return list(
            map(operator.eq, collection, itertools.repeat(target_element))
        ).index(True)
    except ValueError:
        return len(collection) - 1


def find_if(collection: Collection, unary_predicate: UnaryPredicate) -> int:
    """
        Find the index of the first element in collection satisfying unary_predicate
    Args:
        collection: A collection which to search through
        unary_predicate: An UnaryPredicate, which determines if the current value is our target

    Returns:
        The index of the first element which satisfies unary_predicate, -1 if no element satisfies unary_predicate
    """
    try:
        return list(map(unary_predicate, collection)).index(True)
    except ValueError:
        return len(collection) - 1


def find_if_not(collection: Collection, unary_predicate: UnaryPredicate) -> int:
    """
        Find the index of the first element in collection NOT satisfying unary_predicate
    Args:
        collection: A collection which to search through
        unary_predicate: An UnaryPredicate, which determines if the current value is NOT our target

    Returns:
        The index of the first element which DOES NOT satisfy unary_predicate, -1 if all elements satisfy unary_predicate
    """
    try:
        return list(map(unary_predicate, collection)).index(False)
    except ValueError:
        return len(collection) - 1


def find_end():
    raise NotImplementedError


def find_first_of():
    raise NotImplementedError


def adjacent_find():
    raise NotImplementedError


def search():
    raise NotImplementedError


def search_n():
    raise NotImplementedError


def copy():
    raise NotImplementedError


def copy_if():
    raise NotImplementedError


def copy_n():
    raise NotImplementedError


def copy_backward():
    raise NotImplementedError


def move():
    raise NotImplementedError


def move_backward():
    raise NotImplementedError


def fill():
    raise NotImplementedError


def fill_n():
    raise NotImplementedError


def transform():
    raise NotImplementedError


def generate():
    raise NotImplementedError


def generate_n():
    raise NotImplementedError


def remove():
    raise NotImplementedError


def remove_if():
    raise NotImplementedError


def remove_copy():
    raise NotImplementedError


def remove_copy_if():
    raise NotImplementedError


def replace():
    raise NotImplementedError


def replace_if():
    raise NotImplementedError


def replace_copy():
    raise NotImplementedError


def replace_copy_if():
    raise NotImplementedError


def swap():
    raise NotImplementedError


def swap_ranges():
    raise NotImplementedError


def iter_swap():
    raise NotImplementedError


def reverse():
    raise NotImplementedError


def reverse_copy():
    raise NotImplementedError


def rotate():
    raise NotImplementedError


def rotate_copy():
    raise NotImplementedError


def shift_left():
    raise NotImplementedError


def shift_right():
    raise NotImplementedError


def random_shuffle():
    raise NotImplementedError


def shuffle():
    raise NotImplementedError


def sample():
    raise NotImplementedError


def unique():
    raise NotImplementedError


def unique_copy():
    raise NotImplementedError


def is_partitioned():
    raise NotImplementedError


def partition():
    raise NotImplementedError


def partition_copy():
    raise NotImplementedError


def stable_partition():
    raise NotImplementedError


def partition_point():
    raise NotImplementedError


def is_sorted():
    raise NotImplementedError


def is_sorted_until():
    raise NotImplementedError


def sort():
    raise NotImplementedError


def partial_sort():
    raise NotImplementedError


def partial_sort_copy():
    raise NotImplementedError


def stable_sort():
    raise NotImplementedError


def nth_element():
    raise NotImplementedError


def lower_bound():
    raise NotImplementedError


def upper_bound():
    raise NotImplementedError


def binary_search():
    raise NotImplementedError


def equal_range():
    raise NotImplementedError


def merge():
    raise NotImplementedError


def implace_merge():
    raise NotImplementedError


def includes():
    raise NotImplementedError


def set_difference():
    raise NotImplementedError


def set_intersection():
    raise NotImplementedError


def set_symmetric_difference():
    raise NotImplementedError


def set_union():
    raise NotImplementedError


def is_heap():
    raise NotImplementedError


def is_heap_until():
    raise NotImplementedError


def make_heap():
    raise NotImplementedError


def push_heap():
    raise NotImplementedError


def pop_heap():
    raise NotImplementedError


def sort_heap():
    raise NotImplementedError


def max():
    raise NotImplementedError


def max_element():
    raise NotImplementedError


def min():
    raise NotImplementedError


def min_element():
    raise NotImplementedError


def minmax():
    raise NotImplementedError


def minmax_element():
    raise NotImplementedError


def clamp():
    raise NotImplementedError


def equal():
    raise NotImplementedError


def lexicographical_compare():
    raise NotImplementedError


def lexicographical_compare_threeway():
    raise NotImplementedError


def is_permutation():
    raise NotImplementedError


def next_permutation():
    raise NotImplementedError


def prev_permutation():
    raise NotImplementedError
