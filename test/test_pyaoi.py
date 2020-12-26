#!/usr/bin/env python3


from typing import List

import pyaoi


class TestAllOf:
    def test_empty(self):
        assert pyaoi.all_of([], None) == True

    def test_true_condition(self):
        assert pyaoi.all_of([1, 2, 3, 4, 5], lambda x: x > 0) == True

    def test_false_condition(self):
        assert pyaoi.all_of([0, 2, 3, 4, 5], lambda x: x > 0) == False


class TestAnyOf:
    def test_empty(self):
        assert pyaoi.any_of([], None) == False

    def test_true_condition(self):
        assert pyaoi.any_of([1, 2, 3, 4, 5], lambda x: x > 0) == True

    def test_false_condition(self):
        assert pyaoi.any_of([0, 2, 3, 4, 5], lambda x: x > 0) == True


class TestNoneOf:
    def test_empty(self):
        assert pyaoi.none_of([], None) == True

    def test_true_condition(self):
        assert pyaoi.none_of([1, 2, 3, 4, 5], lambda x: x > 0) == False

    def test_false_condition(self):
        assert pyaoi.none_of([0, 2, 3, 4, 5], lambda x: x > 0) == True


class TestForEach:
    def test_increment(self):
        collection: List[int] = [1, 2, 3, 4, 5]

        pyaoi.for_each(collection, lambda x: x + 1, False)

        assert collection == [2, 3, 4, 5, 6]

    def test_sum(self):
        collection: List[int] = [1, 2, 3, 4, 5]
        sum: int = 0

        def _add(x: int):
            nonlocal sum
            sum += x

        pyaoi.for_each(collection, _add)

        assert sum == 15 and collection == [1, 2, 3, 4, 5]


class TestForEachN:
    def test_increment(self):
        collection: List[int] = [1, 2, 3, 4, 5]

        pyaoi.for_each_n(collection, lambda x: x + 1, 2, False)

        assert collection == [2, 3, 3, 4, 5]

    def test_sum(self):
        collection: List[int] = [1, 2, 3, 4, 5]

        sum: int = 0

        def _add(x: int):
            nonlocal sum
            sum += x

        pyaoi.for_each_n(collection, _add, 2)

        assert sum == 3 and collection == [1, 2, 3, 4, 5]


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


class TestMismatch:
    def test_one_collection_empty(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], []) is None

    def test_both_collections_empty(self):
        assert pyaoi.mismatch([], []) is None

    def test_no_difference(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (5, 5)

    def test_no_difference_and_second_collection_longer(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]) == (5, 5)

    def test_last_is_different(self):
        assert pyaoi.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == (5, 6)


class TestFind:
    def test_not_present(self):
        assert pyaoi.find([1, 2, 3, 4, 5], 6) == 4

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
        assert pyaoi.find_if([1, 2, 3, 4, 5], lambda x: x > 6) == 4

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
        assert pyaoi.find_end([1, 2, 3], [1, 2, 3, 4]) == 2


class TestFindFirstOf:
    def test_last_index(self):
        assert pyaoi.find_first_of([1, 2, 4, 1, 2, 4, 1, 2, 3], [1, 2, 3]) == 6

    def test_first_index(self):
        assert pyaoi.find_first_of([1, 2, 3, 1, 2, 3], [1, 2, 3]) == 0

    def test_third_index(self):
        assert pyaoi.find_first_of([1, 1, 1, 2, 3, 4, 5, 6], [1, 2, 3]) == 2

    def test_not_present(self):
        assert pyaoi.find_first_of([1, 2, 3], [1, 2, 3, 4]) == 2


class TestAdjacentFind:
    def test_not_present(self):
        assert pyaoi.adjacent_find([1, 2, 3, 4, 5]) == 4

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
        assert pyaoi.search([1, 2, 3, 4, 5], [7, 8]) == 4

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
        assert pyaoi.search_n([1, 2, 3, 4, 5], 6, 2) == 4

    def test_super_empty(self):
        assert pyaoi.search_n([], 10, 5) == -1

    def test_custom_binary_predicate_second(self):
        assert pyaoi.search_n(
            [(1, 2), (3, 4), (3, 4), (5, 6)],
            (3, 4),
            2,
            lambda x, y: x[0] == y[1] and x[1] == y[1],
        )