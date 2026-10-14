import pytest
from two_sum import two_sum


@pytest.mark.parametrize("numbers,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 3], 6, [0, 1]),
    ([3], 6, None),
    ([], 0, None),
    ([0, 0], 0, [0, 1]),
    ([-3, 4, 3, 90], 0, [0, 2]),
])
def test_two_sum(numbers, target, expected):
    before = numbers.copy()
    assert two_sum(numbers, target) == expected
    assert numbers == before
