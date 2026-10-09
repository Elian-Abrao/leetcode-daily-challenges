class _Node:
    """A single node in the singly linked list."""
    __slots__ = ("val", "next")

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        # Use a sentinel (dummy) head to simplify edge cases.
        self._head = _Node()
        self._size = 0

    def _get_node(self, index: int) -> _Node:
        """Return the node at the given 0-based index (assumes index is valid)."""
        # index is within [0, self._size-1], so we need to move index+1 steps
        # from the sentinel to reach the actual node.
        current = self._head
        for _ in range(index + 1):
            current = current.next
        return current

    def get(self, index: int) -> int:
        """Return the value of the index-th node, or -1 if index is invalid."""
        if index < 0 or index >= self._size:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        """Insert a new node before the first element."""
        # Insert directly after the sentinel.
        new_node = _Node(val, self._head.next)
        self._head.next = new_node
        self._size += 1

    def addAtTail(self, val: int) -> None:
        """Append a new node at the end of the list."""
        # Reuse addAtIndex with index == size, which appends after the last node.
        self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Insert a new node before the index-th node.
        If index equals the length, append at the end.
        If index is greater than the length, do nothing.
        """
        if index < 0 or index > self._size:
            return

        # Traverse to the predecessor of the insertion point.
        current = self._head
        for _ in range(index):
            current = current.next

        new_node = _Node(val, current.next)
        current.next = new_node
        self._size += 1

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node if the index is valid."""
        if index < 0 or index >= self._size:
            return

        # Find the predecessor of the node to delete.
        current = self._head
        for _ in range(index):
            current = current.next

        # Skip over the node to remove.
        current.next = current.next.next
        self._size -= 1