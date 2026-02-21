from __future__ import annotations

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        leftmost = root

        while leftmost:
            class _Dummy:
                def __init__(self):
                    self.next = None
            dummy = _Dummy()
            tail = dummy

            curr = leftmost
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next

            leftmost = dummy.next

        return root