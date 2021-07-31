#!/usr/bin/env python3
"""A collection of functions operating on iterables."""
# Copyright 2020-2021 Jonas Muehlmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import collections
import itertools
import operator
from collections import deque
from itertools import chain
from typing import (
    Any,
    Callable,
    Collection,
    Deque,
    Iterable,
    MutableSequence,
    Optional,
    Sequence,
    Sized,
    Tuple,
)

UnaryPredicate = Callable[[Any], bool]
"""A callable that takes one argument and returns a bool"""

BinaryPredicate = Callable[[Any, Any], bool]
"""A callable that takes two arguments and returns a bool"""

UnaryFunction = Callable[[Any], None]
"""A callable that takes one argument and returns none"""


def all_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """Check if an unary predicate returns True for all elements in the iterable.

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for every element in the iterable, False otherwise or if the iterable is empty
    """

    return False if not iterable else all(map(unary_predicate, iterable))


def any_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """Check if an unary predicate returns True for any elements in the iterable.

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for any element in the iterable, False otherwise or if the iterable is empty
    """

    return False if not iterable else any(map(unary_predicate, iterable))


def none_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """Check if an unary predicate returns True for no elements in the iterable.

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for no element in the iterable or if the iterable is empty, False otherwise
    """

    return True if not iterable else not all(map(unary_predicate, iterable))


def for_each(
    iterable: Iterable,
    unary_function: UnaryFunction,
) -> None:
    """Apply an unary function to each element in the iterable.

    This function has read-only access to the iterable

    Args:
        iterable: An iterable to apply the unary_function to
        unary_function: An unary function to apply to each element in the iterable
    """

    for element in iterable:
        unary_function(element)


def for_each_n(
    sequence: Sequence,
    unary_function: UnaryFunction,
    num_elements: int,  # noqa: VNE001,C0103
) -> None:
    """Apply an unary function to the first num_elements elements in the sequence, modifying the elements.

    This function has read-only access to the sequence

    Args:
        sequence: A sequence to apply the unary_function to
        unary_function: An unary function to apply to each element in the sequence
        num_elements: A number indicating the number of elements (counted from the start) to apply the unary_function to
    """

    for element in sequence[:num_elements]:
        unary_function(element)


def count(sequence: Sequence, target: Any) -> int:
    """Count how often target appears in sequence.

    Args:
        sequence: An iterable in which occurrences of target are counted
        target: A value/object, which occurrences will be counted

    Returns:
        How often target appeared in sequence
    """

    return sequence.count(target)


def count_if(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """Count for how many elements in a iterable an unary predicate returns True.

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns True
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns True

    Returns:
        For how many items unary predicate returned True
    """

    return sum(map(unary_predicate, iterable))


def count_if_not(collection: Collection, unary_predicate: UnaryPredicate) -> int:
    """Count for how many elements in a collection an unary predicate returns False.

    Args:
        collection: An collection for which to count for how many elements unary_predicate returns False
        unary_predicate: A value/object, for which to count for how many items in the collection it returns False

    Returns:
        For how many items unary predicate returned False
    """

    return len(collection) - sum(map(unary_predicate, collection))


def mismatch(
    sequence1: Sequence,
    sequence2: Sequence,
    binary_predicate: BinaryPredicate = operator.eq,
) -> Optional[Tuple[Any, Any]]:  # noqa E1136
    """Find the first pair of elements from both sequences, that are considered not equal.

    Only indices until the last one of the shortest sequence are compared.

    Args:
        sequence1: First sequence to use for comparison
        sequence2: Second sequence to use for comparison
        binary_predicate: A binary predicate, that returns true if the elements from both sequences are considered equal
           Defaults to: operator.eq

    Returns:
        None, if one or more sequences is empty, or they do not differ until the end of the shortest sequence.
            If one index has elements that are not considered equal, a Tuple of those elements will be returned

    Example:
        mismatch([], []) returns None since both sequences are empty

        mismatch([1, 2, 3, 4, 5], []) returns None, since one sequence is empty

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) returns None, since both sequences are considered equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) returns (5, 6), the values at the fifth index, since  their fifth index is considered not equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7, 8, 9]) returns (5, 6) for the same reason.
            Since one sequence is longer, it's additional elements are not compared
    """

    if not sequence1 or not sequence2:
        return None

    return next(
        (pair for pair in zip(sequence1, sequence2) if not binary_predicate(*pair)),
        None,
    )


def find(sequence: Sequence, target_element: Any) -> int:
    """Find the index of the first occurrence of target_element in sequence.

    Args:
        sequence: A sequence which to search through
        target_element: An element to search in the sequence

    Returns:
        The index of target_element's first occurrence, -1 if it was not found or the sequence is empty
    """

    if not sequence:
        return -1

    try:
        return sequence.index(target_element)

    except ValueError:
        return -1


def find_if(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """Find the index of the first element in iterable satisfying unary_predicate.

    Args:
        iterable: A iterable which to search through
        unary_predicate: An UnaryPredicate, which determines if the current value is our target

    Returns:
        The index of the first element which satisfies unary_predicate, -1 if no element satisfies unary_predicate or the iterable is empty
    """

    if not iterable:
        return -1

    for i, val in enumerate(iterable):  # noqa: VNE002
        if unary_predicate(val):
            return i

    return -1


def find_if_not(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """Find the index of the first element in iterable NOT satisfying unary_predicate.

    Args:
        iterable: A iterable which to search through
        unary_predicate: An UnaryPredicate, which determines if the current value is NOT our target

    Returns:
        The index of the first element which DOES NOT satisfy unary_predicate, -1 if all elements satisfy unary_predicate or the iterable is empty
    """

    if not iterable:
        return -1

    for i, val in enumerate(iterable):  # noqa: VNE002
        if not unary_predicate(val):
            return i

    return -1


def find_end(
    collection_super: Collection,
    collection_sub: Collection,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Find index of the beginning of the last occurrence of collection_sub in collection_super.

    Args:
        collection_super: A Collection in which to search for the collection_sub
        collection_sub: A Collection to search for in collection_super
        binary_predicate: A BinaryPredicate used to check if an index's elements of both collections are considered equal, defaults to: operator.eq

    Returns:
        The index of the beginning of the last occurrence of collection_sub in collection_super,
            -1 if any of the two collections is empty, or collection_sub does not occur once in collection_super

    """

    if not collection_super or not collection_sub:
        return -1

    for i in range(  # noqa: VNE001
        (len(collection_super) - 1) - (len(collection_sub) - 1), -1, -1
    ):
        if binary_predicate(
            collection_super[i : i + len(collection_sub)], collection_sub  # noqa E203
        ):
            return i

    return -1


def find_first_of(
    iterable_super: Iterable,
    iterable_sub: Iterable,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Find first index in values_in at which an element of iterable_sub occurs.

    Args:
        iterable_super: A Iterable in which to search for values of iterable_sub
        iterable_sub: A Iterable of values to search for in values_in
        binary_predicate: A BinaryPredicate used to check if an index's elements of both Iterables are considered equal, defaults to: operator.eq

    Returns:
        The first index in values_in at which an element of iterable_sub occurs,
            or -1 if any of the two iterables is empty or iterable_sub does not occur once in iterable_super
    """

    if not iterable_super or not iterable_sub:
        return -1

    for i, element_super in enumerate(iterable_super):  # noqa: VNE001
        for element_sub in iterable_sub:
            if binary_predicate(element_super, element_sub):
                return i

    return -1


def adjacent_find(
    sequence: Sequence, binary_predicate: BinaryPredicate = operator.eq
) -> int:
    """Find the first index at which two adjacent elements are considered equal.

    Args:
        sequence: a sequence to search through
        binary_predicate: a binary predicate to evaluate the equality of adjacent elements, defaults to: operator.eq

    Returns:
        The first index at which two adjacent elements are considered equal,
            or -1 if the sequence is empty or no two adjacent elements are considered equal
    """

    if not sequence:
        return -1
    try:
        # Multiplying index by two, since the list resulting from the call to map has
        # half the length of the input, since it is sliced in half

        return (
            list(map(binary_predicate, sequence[::2], sequence[1::2])).index(True) * 2
        )
    except ValueError:
        return -1


def search(
    sequence_super: Sequence,
    sequence_sub: Sequence,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Search for the first occurrence of sequence_sub in sequence_super.

    Args:
        sequence_super: A sequence to search in
        sequence_sub: A sequence to search for in sequence_super
        binary_predicate: A binary predicate to evaluate the equality of compared items, defaults to: operator.eq

    Returns:
        The index of the beginning of the first occurrence of sequence_sub in sequence_super,
            or -1 if any sequence_super or sequence_sub is empty or sequence_sub does not occur once in sequence_super
    """

    if not sequence_super or not sequence_sub:
        return -1

    for i in range(len((sequence_super))):  # noqa: VNE001
        for element_super, element_sub in zip(sequence_super[i:], sequence_sub):
            if not binary_predicate(element_super, element_sub):
                break

            return i

    return -1


def search_n(
    sequence: Sequence,
    value: Any,  # noqa: VNE002
    num_elements: int,  # noqa: VNE001
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Search for the first occurrence of num_elements repetitions of value in sequence.

    Args:
        sequence: A sequence to search in
        value: any object to search for in collection
        num_elements: How many times, counting from the beginning, value has to be repeated
        binary_predicate: A binary predicate to evaluate the equality of consecutive items, defaults to: operator.eq

    Returns:
        The index of the beginning of the first num_elements repetitions of value in sequence,
            or -1 if sequence is empty or value does not occur once in sequence
    """

    if not sequence:
        return -1

    for i in range(len((sequence))):  # noqa: VNE001
        for element in sequence[i : i + num_elements]:  # noqa: E203
            if not binary_predicate(element, value):
                break
        else:
            return i

    return -1


def copy_replace(iterable: Iterable, old_val: Any, new_val: Any) -> Iterable:
    """Copy iterable while replacing all occurrences of old_val with new_val.

    Args:
        iterable: An iterable to copy
        old_val: A value to replace
        new_val: A value serving as the replacement

    Returns:
        A generator yielding the values of iterable with all occurrences of old_val replaced with new_val
    """

    return (val if val != old_val else new_val for val in iterable)


def copy_replace_if(
    iterable: Iterable, unary_predicate: UnaryPredicate, new_val: Any
) -> Iterable:
    """Copy iterable while replacing all values satisfying unary_predicate with new_val.

    Args:
        iterable: An iterable to copy
        unary_predicate: An unary predicate deciding whether to replace an item
        new_val: A value serving as the replacement

    Returns:
        A generator yielding the values of iterable with all values satisfying unary_predicate replaced with new_val
    """

    return (new_val if unary_predicate(val) else val for val in iterable)


def copy_replace_if_not(
    iterable: Iterable, unary_predicate: UnaryPredicate, new_val: Any
) -> Iterable:
    """Copy iterable while replacing all values not satisfying unary_predicate with new_val.

    Args:
        iterable: An iterable to copy
        unary_predicate: An unary predicate deciding whether to replace an item
        new_val: A value serving as the replacement

    Returns:
        A generator yielding the values of iterable with all values not satisfying unary_predicate replaced with new_val
    """

    return (new_val if not unary_predicate(val) else val for val in iterable)


def copy_except(iterable: Iterable, exclude: Any) -> Iterable:
    """Copy iterable while excluding all occurrences of exclude.

    Args:
        iterable: An iterable to copy
        exclude: A value to exclude

    Returns:
        A generator yielding the values of iterable except exclude
    """

    return (val for val in iterable if val != exclude)


def copy_except_if(iterable: Iterable, unary_predicate: UnaryPredicate) -> Iterable:
    """Copy iterable while excluding all values satisfying unary_predicate.

    Args:
        iterable: An iterable to copy
        unary_predicate: An unary predicate deciding whether to exclude a value

    Returns:
        A generator yielding the values of iterable except the ones satisfying unary_predicate
    """

    return (val for val in iterable if not unary_predicate(val))


def copy_except_if_not(iterable: Iterable, unary_predicate: UnaryPredicate) -> Iterable:
    """Copy iterable while excluding all values not satisfying unary_predicate.

    Args:
        iterable: An iterable to copy
        unary_predicate: An unary predicate deciding whether to exclude a value

    Returns:
        A generator yielding the values of iterable except the ones not satisfying unary_predicate
    """

    return (val for val in iterable if unary_predicate(val))


def fill_n(sequence: Sequence, val: Any, num_elements: int) -> chain:  # noqa: VNE002
    """Set the first num_elements indices of sequence to val.
    Args:
        sequence: A sequence to fill
        val: A value to set indices of sequence to
        num_elements: A value indicating how many indices(counted from the beginning) to set to val
    Returns:
        An iterable with the first num_elements elements changed to val
    """

    return itertools.chain(
        itertools.repeat(
            val,
            num_elements if num_elements < len(sequence) else len(sequence),
        ),
        sequence[num_elements:],
    )


def map_n(
    sequence: Sequence, unary_function: UnaryFunction, num_elements: int
) -> chain:
    """Change the first num_elements elements in sequence by passing them to unary_function and replacing them by the return values.

    Args:
        sequence: A sequence to modify
        unary_function: A function returning new values for each element
        num_elements: A value indicating the number of elements(counted from the beginning) to transform
    Returns:
        An iterable with the first num_elements elements changed by unary_function
    """

    return chain(map(unary_function, sequence[:num_elements]), sequence[num_elements:])


def rotate_copy(iterable: Iterable, n: int) -> Deque:
    """Return a deque of iterable with it's content rotated n places to the right.

    iterable: An iterable to rotate
    n: The number of places to rotate the iterable (negative values rotate to the left)
    """
    deq: Deque = collections.deque(iterable)
    deq.rotate(n)

    return deq


def shift_left(sized: Sized, n: int) -> Sized:
    """Return a copy of sized with it's elements shifted n places to the right but keeping the same size.
    sized: A sized object which's elements to shift
    n: How many places to shift sized's items to the right
    """

    return sized[: len(sized) - n] + [None] * n


def shift_right(sized: Sized, n: int) -> Sized:
    """Return a copy of sized with it's elements shifted n places to the left but keeping the same size.
    sized: A sized object which's elements to shift
    n: How many places to shift sized's items to the left
    """

    return [None] * n + sized[n : len(sized)]
