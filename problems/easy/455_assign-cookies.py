from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # If there are no children or no cookies, nothing can be content.
        if not g or not s:
            return 0

        # Sort both arrays to enable a greedy, two-pointer pass.
        g.sort()
        s.sort()

        child = 0  # index for g (greed factors)
        cookie = 0  # index for s (cookie sizes)
        content = 0  # number of content children

        # Greedily assign the smallest available cookie that satisfies each child.
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                content += 1
                child += 1  # this child is content, move to next child
                cookie += 1  # use this cookie, move to next cookie
            else:
                # Current cookie too small for this child, try a larger cookie
                cookie += 1

        return content