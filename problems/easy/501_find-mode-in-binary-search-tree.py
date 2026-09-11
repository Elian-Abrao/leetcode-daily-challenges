from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        modes = []
        max_count = 0
        prev_val = None
        cur_count = 0

        cur = root
        while cur:
            if not cur.left:
                if prev_val is None or cur.val != prev_val:
                    if prev_val is not None:
                        if cur_count > max_count:
                            modes = [prev_val]
                            max_count = cur_count
                        elif cur_count == max_count:
                            modes.append(prev_val)
                    prev_val = cur.val
                    cur_count = 1
                else:
                    cur_count += 1
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev_val is None or cur.val != prev_val:
                        if prev_val is not None:
                            if cur_count > max_count:
                                modes = [prev_val]
                                max_count = cur_count
                            elif cur_count == max_count:
                                modes.append(prev_val)
                        prev_val = cur.val
                        cur_count = 1
                    else:
                        cur_count += 1
                    cur = cur.right

        if prev_val is not None:
            if cur_count > max_count:
                modes = [prev_val]
            elif cur_count == max_count:
                modes.append(prev_val)

        return modes