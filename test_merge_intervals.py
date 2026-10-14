from copy import deepcopy
import pytest
from merge_intervals import merge_intervals


@pytest.mark.parametrize("intervals,expected", [
    ([[1, 3], [2, 6], [8, 10]], [[1, 6], [8, 10]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[5, 8], [1, 6]], [[1, 8]]),
    ([], []),
    ([[1, 1], [1, 1]], [[1, 1]]),
])
def test_merge_intervals(intervals, expected):
    before = deepcopy(intervals)
    assert merge_intervals(intervals) == expected
    assert intervals == before
