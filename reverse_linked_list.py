class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    """Reverse an acyclic singly linked list in place, returning its new head."""
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return head
