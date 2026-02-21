from __future__ import annotations
from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # Convert to mutable list for easy updates
        n = len(s)
        arr = list(s)
        k = len(queryCharacters)
        
        # Segment tree storage for maintaining longest repeating substring information
        size = 4 * max(1, n)
        leftChar = [''] * size
        rightChar = [''] * size
        leftRun = [0] * size        # length of prefix with same character as leftChar
        rightRun = [0] * size       # length of suffix with same character as rightChar
        best = [0] * size           # best (longest) repeating substring within interval
        segLen = [0] * size         # length of the interval represented by this node

        # Build the segment tree
        def build(node: int, l: int, r: int):
            segLen[node] = r - l + 1
            if l == r:
                ch = arr[l]
                leftChar[node] = ch
                rightChar[node] = ch
                leftRun[node] = rightRun[node] = best[node] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node)

        # Merge two child nodes to form the parent node
        def pull(node: int):
            left = node * 2
            right = left + 1
            
            # Inherit boundary characters from children
            leftChar[node] = leftChar[left]
            rightChar[node] = rightChar[right]
            # Interval length
            segLen[node] = segLen[left] + segLen[right]

            # Compute leftRun for the parent
            # If entire left child is a single run and its character matches the start of right child
            if leftRun[left] == segLen[left] and rightChar[left] == leftChar[right]:
                leftRun[node] = segLen[left] + leftRun[right]
            else:
                leftRun[node] = leftRun[left]

            # Compute rightRun for the parent
            # If entire right child is a single run and its character matches the end of left child
            if rightRun[right] == segLen[right] and rightChar[left] == rightChar[right]:
                rightRun[node] = segLen[right] + rightRun[left]
            else:
                rightRun[node] = rightRun[right]

            # Compute best (longest) by considering cross boundary
            cross = 0
            if rightChar[left] == leftChar[right]:
                cross = rightRun[left] + leftRun[right]
            best[node] = max(best[left], best[right], cross)

        # Point update: set position idx to value val
        def update(node: int, l: int, r: int, idx: int, val: str):
            if l == r:
                leftChar[node] = rightChar[node] = val
                leftRun[node] = rightRun[node] = best[node] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            pull(node)

        # Edge case: empty string (not expected per constraints, but safe)
        if n == 0:
            return []

        # Build initial tree
        build(1, 0, n - 1)

        res: List[int] = []
        for i in range(k):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            # If the character changes, apply update; otherwise, result remains same
            if arr[idx] != ch:
                arr[idx] = ch
                update(1, 0, n - 1, idx, ch)
            # After this query, best[1] holds the answer for the whole string
            res.append(best[1])

        return res