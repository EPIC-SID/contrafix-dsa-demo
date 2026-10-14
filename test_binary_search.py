import pytest
from binary_search import binary_search


@pytest.mark.parametrize("numbers,target,expected", [
    ([1, 3, 5, 7, 9], 5, 2),
    ([1, 3, 5, 7, 9], 9, 4),
    ([1, 3, 5, 7, 9], 1, 0),
    ([7], 7, 0),
    ([], 7, -1),
    ([1, 3, 5], 4, -1),
])
def test_binary_search(numbers, target, expected):
    before = numbers.copy()
    assert binary_search(numbers, target) == expected
    assert numbers == before
