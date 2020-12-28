#!/usr/bin/env python3
"""A collection of functions operating on iterables."""
#  This file is part of pyaoi.
#  Copyright (C) 2020 Jonas Muehlmann
#
#      pyaoi is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      pyaoi is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with pyaoi.  If not, see <https://www.gnu.org/licenses/>.
#
#      pyaoi is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      pyaoi is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with pyaoi.  If not, see <https://www.gnu.org/licenses/>.
#


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
    """Check if an unary predicate returns True for all elements in the iterable, or if the iterable is empty.

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for every element in the iterable, or the iterable is empty, False otherwise
    """
    return all(map(unary_predicate, iterable))


def any_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """Check if an unary predicate returns True for any elements in the iterable, or if the iterable is empty.

    Args:
        iterable: An iterable to apply the unary_predicate to
        unary_predicate: An unary predicate to apply to each element in the iterable

    Returns:
        True if the predicate evaluates to True for any element in the iterable, False otherwise or when the iterable is empty
    """
    return any(map(unary_predicate, iterable))


def none_of(iterable: Iterable, unary_predicate: UnaryPredicate) -> bool:
    """Check if an unary predicate returns False for any elements in the iterable, or if the iterable is empty.

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
    """Apply an unary function to each element in the mutable_sequence, modifying the elements.

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
    num_elements: int,  # noqa: VNE001,C0103
    readonly: bool = True,
) -> None:
    """Apply an unary function to the first num_elements elements in the mutable_sequence, modifying the elements.

    Args:
        mutable_sequence: A mutable iterable to apply the unary_function to
        unary_function: An unary function to apply to each element in the mutable_sequence
        num_elements: A number indicating the number of elements (counted from the start) to apply the unary_function to
        readonly: indicates whether the mutable_sequence is intended to be read or modified,defaults to True
    """
    if readonly:
        for element in mutable_sequence[:num_elements]:
            unary_function(element)
    else:
        mutable_sequence[:num_elements] = list(
            map(unary_function, mutable_sequence[:num_elements])
        )


def count(sequence: Sequence, target: Any) -> int:
    """Count how often target appears in sequence.

    Args:
        sequence: An iterable in which occurrences of target are counted
        target: A value/object, which's occurrences will be counted

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


def count_if_not(iterable: Iterable, unary_predicate: UnaryPredicate) -> int:
    """Count for how many elements in a iterable an unary predicate returns False.

    Args:
        iterable: An iterable for which to count for how many elements unary_predicate returns False
        unary_predicate: A value/object, for which to count for how many items in the iterable it returns False

    Returns:
        For how many items unary predicate returned False, -1 if the iterable is empty
    """
    return (
        -1
        if not iterable
        else sum(map(lambda element: not unary_predicate(element), iterable))
    )


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
            If not provided, operator.eq will be used as a binary_predicate

    Returns:
        None, if one or more sequences is empty, or they do not differ until the end of the shortest sequence.
            If one index has elements that are not considered equal, a Tuple of those elements will be returned

    Example:
        mismatch([], []) returns None since both sequences are empty

        mismatch([1, 2, 3, 4, 5], []) returns None, since one sequence is empty

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) returns None, since both sequences are considered equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) returns (5, 6), since  their fifth index is considered not equal

        mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7, 8, 9]) returns (5, 6), since  their fifth index is considered not equal.
        Since one sequence is longer, it's additional elements are not compared
    """
    if not sequence1 or not sequence2:
        return None
    last_index_shortest_sequence: int = min(len(sequence1), len(sequence2)) - 1

    return next(
        (pair for pair in zip(sequence1, sequence2) if not binary_predicate(*pair)),
        (
            sequence1[last_index_shortest_sequence],
            sequence2[last_index_shortest_sequence],
        ),
    )


def find(collection: Collection, target_element: Any) -> int:
    """Find the index of the first occurrence of target_element in collection.

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
    """Find the index of the first element in collection satisfying unary_predicate.

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
    """Find the index of the first element in collection NOT satisfying unary_predicate.

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


def find_end(
    collection_super: Collection,
    collection_sub: Collection,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Find index of the beginning of the last occurrence of collection_sub in collection_super.

    Args:
        collection_super: A Collection in which to search for the collection_sub
        collection_sub: A Collection to search for in collection_super
        binary_predicate: A BinaryPredicate used to check if an index's elements of both collections are considered equal

    Returns:
        The index of the beginning of the last occurrence of collection_sub in collection_super,
            or the last index in collection_super if it is empty or collection_sub is not found in it

    """
    for i in range(  # noqa: VNE001
        (len(collection_super) - 1) - (len(collection_sub) - 1), -1, -1
    ):
        if binary_predicate(
            collection_super[i : i + len(collection_sub)], collection_sub  # noqa E203
        ):
            return i

    return len(collection_super) - 1


def find_first_of(
    values_in: Collection,
    values_from: Collection,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Find first index in values_in at which an element of values_from occurs.

    Args:
        values_in: A Collection in which to search for values of values_from
        values_from: A Collection of values to search for in values_in
        binary_predicate: A BinaryPredicate used to check if an index's elements of both collections are considered equal

    Returns:
        The first index in values_in at which an element of values_from occurs
            or the last index in  values_in if it is empty or no element from values_from is found in it

    """
    for i, element_in in enumerate(values_in):  # noqa: VNE001
        for element_from in values_from:
            if binary_predicate(element_in, element_from):
                return i

    return len(values_in) - 1


def adjacent_find(
    sequence: Sequence, binary_predicate: BinaryPredicate = operator.eq
) -> int:
    """Find the first index at which two adjacent elements are considered equal.

    Args:
        sequence: a sequence to search through
        binary_predicate: a binary predicate to evaluate the equality of adjacent elements

    Returns:
        The first index at which two adjacent elements are considered equal,
            or the last index, if no two adjacent elements are considered equal,
            or -1 if the sequence is empty

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
        return len(sequence) - 1


def search(
    sequence_super: Sequence,
    sequence_sub: Sequence,
    binary_predicate: BinaryPredicate = operator.eq,
) -> int:
    """Search for the first occurrence of sequence_sub in sequence_super.

    Args:
        sequence_super: A sequence to search in
        sequence_sub: A sequence to search for in sequence_super
        binary_predicate: A binary predicate to evaluate the equality of compared items

    Returns:
        The index of the beginning of the first occurrence of sequence_sub in sequence_super
            If not found, returns the last index of sequence_super
            If any sequence is empty, returns -1
    """
    if not sequence_sub:
        return -1

    for i in range(len((sequence_super))):  # noqa: VNE001
        for element_super, element_sub in zip(sequence_super[i:], sequence_sub):
            if not binary_predicate(element_super, element_sub):
                break

            return i

    return len(sequence_super) - 1


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
        binary_predicate: A binary predicate to evaluate the equality of consecutive items

    Returns:
        The index of the beginning of the first num_elements repetitions of value in sequence
            If not found, returns the last index of sequence_super
            If sequence is empty, returns -1
    """
    if not sequence:
        return -1

    for i in range(len((sequence))):  # noqa: VNE001
        for element in sequence[i : i + num_elements]:  # noqa: E203
            if not binary_predicate(element, value):
                break
        else:
            return i

    return len(sequence) - 1
