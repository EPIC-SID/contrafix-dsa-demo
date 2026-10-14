import pytest
from balanced_brackets import balanced_brackets


@pytest.mark.parametrize("text,expected", [
    ("([]{})", True),
    ("", True),
    ("(", False),
    ("([)]", False),
    (")", False),
    ("price[items", False),
    ("a + (b[c] * {d})", True),
])
def test_balanced_brackets(text, expected):
    assert balanced_brackets(text) is expected
