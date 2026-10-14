import pytest
from largest_element import largest_element


@pytest.mark.parametrize("numbers,expected", [
    ([3, 9, 2], 9),
    ([-8, -3, -6], -3),
    ([-5], -5),
    ([0, 0], 0),
    ([2, 2, 1], 2),
    ([], None),
])
def test_largest_element(numbers, expected):
    before = numbers.copy()
    assert largest_element(numbers) == expected
    assert numbers == before
