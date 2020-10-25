"""A pure python implementation of the C++ Standard Template Library(STL)'s algorithm header"""
#!/usr/bin/env python3
# !/usr/bin/env python3
import operator
from typing import Iterable, Callable, Any, MutableSequence, Tuple, Optional

from src import util
# !/usr/bin/env python3
# !/usr/bin/env python3
import operator
from typing import Iterable, Callable, Any, MutableSequence, Tuple, Optional

from src import util

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


def for_each(mutable_sequence: MutableSequence, unary_function: UnaryFunction) -> None:
    """
    Apply an unary function to each element in the mutable_sequence, modifying the elements

    Args:
        mutable_sequence: A mutable sequence to apply the unary_function to
        unary_function: An unary function to apply to each element in the mutable_sequence
    """
    if util.is_lambda(unary_function) or util.contains_explicit_return(unary_function):
        for i, element in enumerate(mutable_sequence):
            mutable_sequence[i] = unary_function(element)
    else:
        for element in mutable_sequence:
            unary_function(element)


def for_each_n(
    mutable_sequence: MutableSequence, unary_function: UnaryFunction, n: int
) -> None:
    """
    Apply an unary function to the first n elements in the mutable_sequence, modifying the elements

    Args:
        mutable_sequence: A mutable sequence to apply the unary_function to
        unary_function: An unary function to apply to each element in the mutable_sequence
        n: A number indicating the number of elements (counted from the start) to apply the unary_function to
    """
    if util.is_lambda(unary_function) or util.contains_explicit_return(unary_function):
        for i, element in enumerate(mutable_sequence[:n]):
            mutable_sequence[i] = unary_function(element)
    else:
        for element in mutable_sequence[:n]:
            unary_function(element)


def count(iterable: Iterable, target: Any) -> int:
    """
    Count how often target appears in iterable

    Args:
        iterable: An iterable in which occurrences of target are counted
        target: A value/object, which's occurrences will be counted

    Returns:
        How often target appeared in iterable
    """
    occurrences: int = 0

    for element in iterable:
        if element == target:
            occurrences += 1

    return occurrences


def count_if(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """
    Count for how many elements in a sequence an unary predicate returns True

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns True
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns True

    Returns:
        For how many items unary predicate returned True
    """
    occurrences: int = 0

    for element in iterable:
        if unary_predicate(element):
            occurrences += 1

    return occurrences


def count_if_not(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """
    Count for how many elements in a sequence an unary predicate returns False

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns False
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns False

    Returns:
        For how many items unary predicate returned False, -1 if the iterable is empty
    """
    if len(iterable) == 0:
        # CHECK: if it makes sense to raise an exception or return None instead
        return -1

    occurrences: int = 0

    for element in iterable:
        if not unary_predicate(element):
            occurrences += 1

    return occurrences


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
    last_pair: Optional[Tuple[Any, Any]] = None
    for last_pair in zip(iterable1, iterable2):
        if not binary_predicate(last_pair[0], last_pair[1]):
            return last_pair
    return last_pair


def find():
    raise NotImplementedError


def find_if():
    raise NotImplementedError


def find_if_not():
    raise NotImplementedError


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
