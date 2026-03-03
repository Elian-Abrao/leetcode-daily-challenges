from __future__ import annotations
from typing import Optional

# LeetCode provides ListNode and TreeNode definitions at runtime.
# The following implementation uses the standard O(n log n) approach:
# repeatedly find the middle node to serve as root, recursing on left and right halves.

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Helper to find the middle node of the linked list segment.
        # Also cuts the left part from the list to form a proper left subtree input.
        def find_middle(start: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            slow = start
            fast = start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            # Cut the left half from the middle to form two independent lists
            if prev is not None:
                prev.next = None
            return slow

        if head is None:
            return None

        mid = find_middle(head)
        root = TreeNode(mid.val)

        # If there is only one element in the list segment, that's the leaf/root.
        if head is mid:
            return root

        # Recursively build left and right subtrees from the split lists.
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root