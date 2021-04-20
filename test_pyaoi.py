#!/usr/bin/env python3


import collections
from typing import List

import pyaoi


class TestAllOf:
    def test_empty(self):
        assert not pyaoi.all_of([], None)

    def test_true_condition(self):
        assert pyaoi.all_of([1, 2, 3, 4, 5], lambda x: x > 0)

    def test_false_condition(self):
        assert not pyaoi.all_of([0, 2, 3, 4, 5], lambda x: x > 0)


class TestAnyOf:
    def test_empty(self):
        assert not pyaoi.any_of([], None)

    def test_true_condition(self):
        assert pyaoi.any_of([1, 2, 3, 4, 5], lambda x: x > 0)

    def test_false_condition(self):
        assert pyaoi.any_of([0, 2, 3, 4, 5], lambda x: x > 0)


class TestNoneOf:
    def test_empty(self):
        assert pyaoi.none_of([], None)

    def test_true_condition(self):
        assert not pyaoi.none_of([1, 2, 3, 4, 5], lambda x: x > 0)

    def test_false_condition(self):
        assert pyaoi.none_of([0, 2, 3, 4, 5], lambda x: x > 0)


class TestForEach:  # noqa: R0903
    def test_sum(self):
        collection: List[int] = [1, 2, 3, 4, 5]
        _sum: int = 0

        def _add(addend: int):
            nonlocal _sum
            _sum += addend

        pyaoi.for_each(collection, _add)

        assert _sum == 15 and collection == [1, 2, 3, 4, 5]


class TestForEachN:  # noqa: R0903
    def test_sum(self):
        collection: List[int] = [1, 2, 3, 4, 5]

        _sum: int = 0

        def _add(addend: int):
            nonlocal _sum
            _sum += addend

        pyaoi.for_each_n(collection, _add, 2)

        assert _sum == 3 and collection == [1, 2, 3, 4, 5]


class TestCount:
    def test_empty_collection(self):
        assert pyaoi.count([], 5) == 0

    def test_0_occurrences(self):
        assert pyaoi.count([1, 2, 3, 4, 5], 0) == 0

    def test_2_occurrences(self):
        assert pyaoi.count([1, 1, 2, 3, 4, 5], 1) == 2


class TestCountIf:
    def test_empty_collection(self):
        assert pyaoi.count_if([], lambda x: x == 1) == 0

    def test_0_occurrences(self):
        assert pyaoi.count_if([1, 2, 3, 4, 5], lambda x: x == 0) == 0

    def test_2_occurrences(self):
        assert pyaoi.count_if([1, 1, 2, 3, 4, 5], lambda x: x == 1) == 2


class TestCountIfNot:
    def test_empty_collection(self):
        assert pyaoi.count_if_not([], lambda x: x == 1) == 0

    def test_0_occurrences(self):
        assert pyaoi.count_if_not([1, 2, 3, 4, 5], lambda x: x > 0) == 0

    def test_2_occurrences(self):
        assert pyaoi.count_if_not([1, 1, 2, 3, 4, 5], lambda x: x > 1) == 2


class TestMismatch:
    def test_one_collection_empty(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], []) is None

    def test_both_collections_empty(self):
        assert pyaoi.mismatch([], []) is None

    def test_no_difference(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) is None

    def test_no_difference_and_second_collection_longer(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]) is None

    def test_last_is_different(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == (5, 6)


class TestFind:
    def test_not_present(self):
        assert pyaoi.find([1, 2, 3, 4, 5], 6) == -1

    def test_first_element(self):
        assert pyaoi.find([1, 2, 3, 4, 5], 1) == 0

    def test_third_element(self):
        assert pyaoi.find([1, 2, 3, 4, 5], 3) == 2

    def test_last_element(self):
        assert pyaoi.find([1, 2, 3, 4, 5], 5) == 4

    def test_empty_collection(self):
        assert pyaoi.find([], 2) == -1


class TestFindIf:
    def test_not_present(self):
        assert pyaoi.find_if([1, 2, 3, 4, 5], lambda x: x > 6) == -1

    def test_first_element(self):
        assert pyaoi.find_if([1, 2, 3, 4, 5], lambda x: x == 1) == 0

    def test_third_element(self):
        assert pyaoi.find_if([1, 2, 3, 4, 5], lambda x: x == 3) == 2

    def test_last_element(self):
        assert pyaoi.find_if([1, 2, 3, 4, 5], lambda x: x == 5) == 4

    def test_empty_collection(self):
        assert pyaoi.find_if([], lambda x: 0 < x < 5) == -1


class TestFindEnd:
    def test_last_index(self):
        assert pyaoi.find_end([1, 2, 3, 1, 2, 3, 1, 2, 3], [1, 2, 3]) == 6

    def test_first_index(self):
        assert pyaoi.find_end([1, 2, 3], [1, 2, 3]) == 0

    def test_third_index(self):
        assert pyaoi.find_end([1, 1, 1, 2, 3], [1, 2, 3]) == 2

    def test_not_present(self):
        assert pyaoi.find_end([1, 2, 3], [1, 2, 3, 4]) == -1

    def test_super_empty(self):
        assert pyaoi.find_end([], [1, 2, 3, 4]) == -1

    def test_both_empty(self):
        assert pyaoi.find_end([], []) == -1


class TestFindFirstOf:
    def test_last_index(self):
        assert pyaoi.find_first_of([1, 2, 4, 1, 2, 4, 1, 2, 3], [3, 6, 9]) == 8

    def test_first_index(self):
        assert pyaoi.find_first_of([1, 2, 3, 1, 2, 3], [1, 2, 3]) == 0

    def test_third_index(self):
        assert pyaoi.find_first_of([-1, -2, 1, 2, 3, 4, 5, 6], [1, 2, 3]) == 2

    def test_not_present(self):
        assert pyaoi.find_first_of(list(range(4)), list(range(5, 10))) == -1

    def test_super_empty(self):
        assert pyaoi.find_first_of([], list(range(5, 10))) == -1

    def test_sub_empty(self):
        assert pyaoi.find_first_of(list(range(4)), []) == -1


class TestAdjacentFind:
    def test_not_present(self):
        assert pyaoi.adjacent_find([1, 2, 3, 4, 5]) == -1

    def test_empty(self):
        assert pyaoi.adjacent_find([]) == -1

    def test_first_pair(self):
        assert pyaoi.adjacent_find([1, 1, 2, 3, 4, 5]) == 0

    def test_last_pair(self):
        assert pyaoi.adjacent_find([1, 2, 3, 4, 5, 5]) == 4


class TestSearch:
    def test_beginning(self):
        assert pyaoi.search([1, 2, 3, 4, 5], [1, 2, 3]) == 0

    def test_end(self):
        assert pyaoi.search([1, 2, 3, 4, 5], [4, 5]) == 3

    def test_third(self):
        assert pyaoi.search([1, 2, 3, 4, 5], [3, 4, 5]) == 2

    def test_not_present(self):
        assert pyaoi.search([1, 2, 3, 4, 5], [7, 8]) == -1

    def test_super_empty(self):
        assert pyaoi.search([], [7, 8]) == -1

    def test_sub_empty(self):
        assert pyaoi.search([1, 2, 3, 4, 5], []) == -1

    def test_custom_binary_predicate_second(self):
        assert pyaoi.search(
            [(1, 2), (3, 4), (5, 6)],
            [(3, 4), (5, 6)],
            lambda x, y: x[0] == y[1] and x[1] == y[1],
        )


class TestSearchN:
    def test_beginning(self):
        assert pyaoi.search_n([1, 1, 1, 2, 3, 4, 5], 1, 2) == 0

    def test_end(self):
        assert pyaoi.search_n([1, 2, 3, 4, 4, 4], 4, 2) == 3

    def test_third(self):
        assert pyaoi.search_n([1, 2, 3, 4, 5], 3, 1) == 2

    def test_not_present(self):
        assert pyaoi.search_n([1, 2, 3, 4, 5], 6, 2) == -1

    def test_super_empty(self):
        assert pyaoi.search_n([], 10, 5) == -1

    def test_custom_binary_predicate_second(self):
        assert pyaoi.search_n(
            [(1, 2), (3, 4), (3, 4), (5, 6)],
            (3, 4),
            2,
            lambda x, y: x[0] == y[1] and x[1] == y[1],
        )


class TestCopyReplace:
    def test_empty(self):
        assert list(pyaoi.copy_replace([], 1, 2)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_replace([1, 2, 3, 4], 5, 6)) == [1, 2, 3, 4]

    def test_last_change(self):
        assert list(pyaoi.copy_replace([1, 2, 3, 4], 4, 6)) == [1, 2, 3, 6]


class TestCopyReplaceIf:
    def test_empty(self):
        assert list(pyaoi.copy_replace_if([], lambda x: x == 0, 2)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_replace_if([1, 2, 3, 4], lambda x: x == 0, 6)) == [
            1,
            2,
            3,
            4,
        ]

    def test_last_change(self):
        assert list(pyaoi.copy_replace_if([1, 2, 3, 4], lambda x: x == 4, 6)) == [
            1,
            2,
            3,
            6,
        ]


class TestCopyReplaceIfNot:
    def test_empty(self):
        assert list(pyaoi.copy_replace_if_not([], lambda x: x == 0, 2)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_replace_if_not([1, 2, 3, 4], lambda x: x < 5, 6)) == [
            1,
            2,
            3,
            4,
        ]

    def test_last_change(self):
        assert list(pyaoi.copy_replace_if_not([1, 2, 3, 4], lambda x: x < 4, 6)) == [
            1,
            2,
            3,
            6,
        ]


class TestCopyExcept:
    def test_empty(self):
        assert list(pyaoi.copy_except([], 2)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_except([1, 2, 3, 4], 5)) == [1, 2, 3, 4]

    def test_last_excluded(self):
        assert list(pyaoi.copy_except([1, 2, 3, 4], 4)) == [1, 2, 3]


class TestCopyExceptIf:
    def test_empty(self):
        assert list(pyaoi.copy_except_if([], lambda x: x == 0)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_except_if([1, 2, 3, 4], lambda x: x == 0)) == [
            1,
            2,
            3,
            4,
        ]

    def test_last_excluded(self):
        assert list(pyaoi.copy_except_if([1, 2, 3, 4], lambda x: x == 4)) == [1, 2, 3]


class TestCopyExceptIfNot:
    def test_empty(self):
        assert list(pyaoi.copy_except_if_not([], lambda x: x == 0)) == []

    def test_no_change(self):
        assert list(pyaoi.copy_except_if_not([1, 2, 3, 4], lambda x: x < 5)) == [
            1,
            2,
            3,
            4,
        ]

    def test_last_excluded(self):
        assert list(pyaoi.copy_except_if_not([1, 2, 3, 4], lambda x: x < 4)) == [
            1,
            2,
            3,
        ]


class TestFill:
    def test_all(self):
        sequence = [1, 2, 3, 4]
        pyaoi.fill(sequence, 5)
        assert sequence == [5, 5, 5, 5]

    def test_empty(self):
        sequence = []
        pyaoi.fill(sequence, 5)
        assert sequence == []


class TestFillN:
    def test_first_2(self):
        sequence = [1, 2, 3, 4]
        pyaoi.fill_n(sequence, 5, 2)
        assert sequence == [5, 5, 3, 4]

    def test_empty(self):
        sequence = []
        pyaoi.fill_n(sequence, 5, 2)
        assert sequence == []


class TestTransform:
    def test_empty(self):
        mutable_sequence = []

        pyaoi.transform(mutable_sequence, lambda x: x + 1)
        assert mutable_sequence == []

    def test_change_all(self):
        mutable_sequence = [1, 2, 3, 4]

        pyaoi.transform(mutable_sequence, lambda x: x + 1)
        assert mutable_sequence == [2, 3, 4, 5]


class TestTransformN:
    def test_empty(self):
        mutable_sequence = []

        pyaoi.transform_n(mutable_sequence, lambda x: x + 1, 5)
        assert mutable_sequence == []

    def test_change_all(self):
        mutable_sequence = [1, 2, 3, 4]

        pyaoi.transform_n(mutable_sequence, lambda x: x + 1, 2)
        assert mutable_sequence == [2, 3, 3, 4]


class TestRotateCopy:
    def test_empty(self):
        assert pyaoi.rotate_copy([], 0) == collections.deque([])

    def test_rotate_0(self):
        assert pyaoi.rotate_copy([1, 2, 3, 4, 5], 0) == collections.deque([1, 2, 3, 4, 5])

    def test_rotate_left(self):
        assert pyaoi.rotate_copy([1, 2, 3, 4, 5], 2) == collections.deque([4, 5, 1, 2, 3])

    def test_rotate_right(self):
        assert pyaoi.rotate_copy([1, 2, 3, 4, 5], -2) == collections.deque([3, 4, 5, 1, 2])


# TODO: Refactor unit tests

class TestShiftLeft:
    def test_empty(self):
        assert pyaoi.shift_left([], 0) == []

    def test_shift_0(self):
        assert pyaoi.shift_left([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

    def test_shift_2(self):
        assert pyaoi.shift_left([1, 2, 3, 4, 5], 2) == [1, 2, 3, None, None]

    def test_shift_len(self):
        assert pyaoi.shift_left([1, 2, 3, 4, 5], 5) == [None] * 5


class TestShifRight:
    def test_empty(self):
        assert pyaoi.shift_right([], 0) == []

    def test_shift_0(self):
        assert pyaoi.shift_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

    def test_shift_2(self):
        assert pyaoi.shift_right([1, 2, 3, 4, 5], 2) == [None, None, 3, 4, 5]

    def test_shift_len(self):
        assert pyaoi.shift_right([1, 2, 3, 4, 5], 5) == [None] * 5
