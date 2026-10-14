import pytest
from linear_search import linear_search


@pytest.mark.parametrize("numbers,target,expected", [
    ([4, 2, 8], 4, 0),
    ([4, 2, 8], 8, 2),
    ([7], 7, 0),
    ([], 7, -1),
    ([2, 2, 3], 2, 0),
    ([1, 2, 3], 9, -1),
])
def test_linear_search(numbers, target, expected):
    before = numbers.copy()
    assert linear_search(numbers, target) == expected
    assert numbers == before
