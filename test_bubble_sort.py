import pytest
from bubble_sort import bubble_sort


@pytest.mark.parametrize("numbers,expected", [
    ([3, 2, 1], [1, 2, 3]),
    ([2, 1], [1, 2]),
    ([], []),
    ([7], [7]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, -1, 0, -3], [-3, -1, 0, 0]),
])
def test_bubble_sort(numbers, expected):
    before = numbers.copy()
    result = bubble_sort(numbers)
    assert result == expected
    assert numbers == before
    assert result is not numbers
