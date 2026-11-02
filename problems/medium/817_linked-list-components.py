from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values = set(nums)
        ans = 0
        inside = False

        cur = head
        while cur:
            if cur.val in values:
                if not inside:
                    ans += 1
                    inside = True
            else:
                inside = False
            cur = cur.next

        return ans