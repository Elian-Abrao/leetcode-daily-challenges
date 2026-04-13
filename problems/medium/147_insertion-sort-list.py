from typing import Optional

# LeetCode provides ListNode; we use it directly in type hints via forward reference strings.

class Solution:
    def insertionSortList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        # Insertion sort builds a new sorted list by repeatedly inserting nodes
        # from the input into the correct position of the sorted part.
        if head is None:
            return None

        # Dummy node simplifies edge cases when inserting at the head.
        dummy = ListNode(0)

        current = head
        while current:
            # Preserve the next node to process before we alter links.
            next_node = current.next

            # Find the insertion point in the already-sorted list.
            # We keep the sorted portion as: dummy -> ... -> tail
            prev = dummy
            # Move forward while the next sorted value is strictly less than current.value
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Move to the next node from the input list
            current = next_node

        return dummy.next