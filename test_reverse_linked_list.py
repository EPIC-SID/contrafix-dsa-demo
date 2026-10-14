import pytest
from reverse_linked_list import Node, reverse_linked_list


@pytest.mark.parametrize("values", [[], [7], [1, 2], [1, 2, 3], [0, -1, 0], [4, 4, 4, 4]])
def test_reverse_linked_list(values):
    nodes = [Node(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    head = reverse_linked_list(nodes[0] if nodes else None)
    for expected, value in zip(reversed(nodes), reversed(values)):
        assert head is expected, "Return the original nodes in reverse order."
        assert head.value == value
        head = head.next
    assert head is None, "The reversed list must end, without a cycle."
