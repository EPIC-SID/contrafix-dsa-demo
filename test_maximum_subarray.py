import pytest
from maximum_subarray import maximum_subarray


@pytest.mark.parametrize("numbers,expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([-8, -3, -6], -3),
    ([-5], -5),
    ([0, 0], 0),
    ([1, 2, 3], 6),
    ([], 0),
])
def test_maximum_subarray(numbers, expected):
    before = numbers.copy()
    assert maximum_subarray(numbers) == expected
    assert numbers == before
