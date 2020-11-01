#!/usr/bin/env python3


from typing import List

from src import std


class TestAllOf:
    def test_empty(self):
        assert std.all_of([], None) == True

    def test_true_condition(self):
        assert std.all_of([1, 2, 3, 4, 5], lambda x: x > 0) == True

    def test_false_condition(self):
        assert std.all_of([0, 2, 3, 4, 5], lambda x: x > 0) == False


class TestAnyOf:
    def test_empty(self):
        assert std.any_of([], None) == False

    def test_true_condition(self):
        assert std.any_of([1, 2, 3, 4, 5], lambda x: x > 0) == True

    def test_false_condition(self):
        assert std.any_of([0, 2, 3, 4, 5], lambda x: x > 0) == True


class TestNoneOf:
    def test_empty(self):
        assert std.none_of([], None) == True

    def test_true_condition(self):
        assert std.none_of([1, 2, 3, 4, 5], lambda x: x > 0) == False

    def test_false_condition(self):
        assert std.none_of([0, 2, 3, 4, 5], lambda x: x > 0) == True


class TestForEach:
    def test_by_addition(self):
        sequence: List[int] = [1, 2, 3, 4, 5]

        std.for_each(sequence, lambda x: x + 1)

        assert sequence == [2, 3, 4, 5, 6]


class TestForEachN:
    def test_by_addition(self):
        sequence: List[int] = [1, 2, 3, 4, 5]

        std.for_each_n(sequence, lambda x: x + 1, 2)

        assert sequence == [2, 3, 3, 4, 5]


class TestCount:
    def test_empty_iterable(self):
        assert std.count([], 5) == 0

    def test_0_occurrences(self):
        assert std.count([1, 2, 3, 4, 5], 0) == 0

    def test_2_occurrences(self):
        assert std.count([1, 1, 2, 3, 4, 5], 1) == 2


class TestCountIf:
    def test_empty_iterable(self):
        assert std.count_if([], lambda x: x == 1) == 0

    def test_0_occurrences(self):
        assert std.count_if([1, 2, 3, 4, 5], lambda x: x == 0) == 0

    def test_2_occurrences(self):
        assert std.count_if([1, 1, 2, 3, 4, 5], lambda x: x == 1) == 2


class TestCountIfNot:
    def test_empty_iterable(self):
        assert std.count_if_not([], lambda x: x == 1) == -1

    def test_0_occurrences(self):
        assert std.count_if_not([1, 2, 3, 4, 5], lambda x: x == 0) == 5

    def test_2_occurrences(self):
        assert std.count_if_not([1, 1, 2, 3, 4, 5], lambda x: x > 1) == 2


class TestMismatch:
    def test_one_iterable_empty(self):
        assert std.mismatch([1, 2, 3, 4, 5], []) is None

    def test_both_iterables_empty(self):
        assert std.mismatch([], []) is None

    def test_no_difference(self):
        assert std.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (5, 5)

    def test_no_difference_and_second_iterable_longer(self):
        assert std.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]) == (5, 5)

    def test_last_is_different(self):
        assert std.mismatch([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == (5, 6)


class TestFind:
    def test_not_present(self):
        assert std.find([1, 2, 3, 4, 5], 6) == 4

    def test_first_element(self):
        assert std.find([1, 2, 3, 4, 5], 1) == 0

    def test_empty_collection(self):
        assert std.find([], 2) == -1


class TestFindIf:
    def test_not_present(self):
        assert std.find_if([1, 2, 3, 4, 5], lambda x: x > 6) == 4

    def test_first_element(self):
        assert std.find_if([1, 2, 3, 4, 5], lambda x: x == 1) == 0

    def test_empty_collection(self):
        assert std.find_if([], lambda x: 0 < x < 5) == -1


class TestFindIfNot:
    def test_not_present(self):
        assert std.find_if_not([1, 2, 3, 4, 5], lambda x: x < 6) == 4

    def test_first_element(self):
        assert std.find_if_not([1, 2, 3, 4, 5], lambda x: x != 1) == 0

    def test_empty_collection(self):
        assert std.find_if_not([], lambda x: 0 < x < 5) == -1


class TestFindEnd:
    pass


class TestFindFirstOf:
    pass


class TestAdjacentFind:
    pass


class TestSearch:
    pass


class TestSearchN:
    pass


class TestCopy:
    pass


class TestCopyIf:
    pass


class TestCopyN:
    pass


class TestCopyBackward:
    pass


class TestMove:
    pass


class TestMoveBackward:
    pass


class TestFill:
    pass


class TestFillN:
    pass


class TestTransform:
    pass


class TestGenerate:
    pass


class TestGenerateN:
    pass


class TestRemove:
    pass


class TestRemoveIf:
    pass


class TestRemoveCopy:
    pass


class TestRemoveCopyIf:
    pass


class TestReplace:
    pass


class TestReplaceIf:
    pass


class TestReplaceCopy:
    pass


class TestReplaceCopyIf:
    pass


class TestSwap:
    pass


class TestSwapRanges:
    pass


class TestIterSwap:
    pass


class TestReverse:
    pass


class TestReverseCopy:
    pass


class TestRotate:
    pass


class TestRotateCopy:
    pass


class TestShiftLeft:
    pass


class TestShiftRight:
    pass


class TestRandomShuffle:
    pass


class TestShuffle:
    pass


class TestSample:
    pass


class TestUnique:
    pass


class TestUniqueCopy:
    pass


class TestIsPartitioned:
    pass


class TestPartition:
    pass


class TestPartitionCopy:
    pass


class TestStablePartition:
    pass


class TestPartitionPoint:
    pass


class TestIsSorted:
    pass


class TestIsSortedUntil:
    pass


class TestSort:
    pass


class TestPartialSort:
    pass


class TestPartialSortCopy:
    pass


class TestStableSort:
    pass


class TestNthElement:
    pass


class TestLowerBound:
    pass


class TestUpperBound:
    pass


class TestBinarySearch:
    pass


class TestEqualRange:
    pass


class TestMerge:
    pass


class TestImplaceMerge:
    pass


class TestIncludes:
    pass


class TestSetDifference:
    pass


class TestSetIntersection:
    pass


class TestSetSymmetricDifference:
    pass


class TestSetUnion:
    pass


class TestIsHeap:
    pass


class TestIsHeapUntil:
    pass


class TestMakeHeap:
    pass


class TestPushHeap:
    pass


class TestPopHeap:
    pass


class TestSortHeap:
    pass


class TestMax:
    pass


class TestMaxElement:
    pass


class TestMin:
    pass


class TestMinElement:
    pass


class TestMinmax:
    pass


class TestMinmaxElement:
    pass


class TestClamp:
    pass


class TestEqual:
    pass


class TestLexicographicalCompare:
    pass


class TestLexicographicalCompareThreeway:
    pass


class TestIsPermutation:
    pass


class TestNextPermutation:
    pass


class TestPrevPermutation:
    pass
