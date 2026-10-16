from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        """
        Splits the linked list into k consecutive parts.
        Parts differ in size by at most 1, and earlier parts are >= later parts.
        Returns a list of k ListNode heads (some may be None).
        """
        # Step 1: Compute total length of the list.
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        # Step 2: Determine base size and how many parts get an extra node.
        base_size = n // k
        extra_parts = n % k  # first 'extra_parts' parts have size base_size + 1

        # Step 3: Build the result.
        result: list[ListNode | None] = []
        current = head  # pointer to traverse the list

        for i in range(k):
            # If we've exhausted the list, remaining parts are None.
            if current is None:
                result.append(None)
                continue

            # Start of the current part.
            part_head = current
            # Determine size of this part.
            part_size = base_size + (1 if i < extra_parts else 0)

            # Advance 'part_size - 1' steps to land on the last node of this part.
            # If part_size == 0, we skip (but part_size >= 1 when current is not None
            # because n >= k at that point? Actually possible if k > n, then we already
            # appended None earlier. So here current is not None, part_size > 0.)
            for _ in range(part_size - 1):
                if current.next:   # safety, should always be valid because part_size <= remaining nodes
                    current = current.next

            # Detach this part from the rest.
            next_part = current.next
            current.next = None
            result.append(part_head)

            # Move to the next segment.
            current = next_part

        return result