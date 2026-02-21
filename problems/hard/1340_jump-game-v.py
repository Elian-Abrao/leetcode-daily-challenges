from __future__ import annotations

from typing import List
import sys

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n  # memoization for max jumps starting from i

        sys.setrecursionlimit(10000)  # safe for n up to 1000

        def dfs(i: int) -> int:
            # If already computed, reuse the result
            if dp[i] != 0:
                return dp[i]

            best = 1  # at least can stay on current index

            # Explore to the right within distance d
            right_limit = min(n, i + d + 1)
            for j in range(i + 1, right_limit):
                # If we encounter a value >= arr[i], we cannot jump further right
                if arr[j] >= arr[i]:
                    break
                candidate = 1 + dfs(j)
                if candidate > best:
                    best = candidate

            # Explore to the left within distance d
            left_limit = max(-1, i - d - 1)
            for j in range(i - 1, left_limit, -1):
                # If we encounter a value >= arr[i], we cannot jump further left
                if arr[j] >= arr[i]:
                    break
                candidate = 1 + dfs(j)
                if candidate > best:
                    best = candidate

            dp[i] = best
            return best

        result = 1
        for i in range(n):
            result = max(result, dfs(i))
        return result