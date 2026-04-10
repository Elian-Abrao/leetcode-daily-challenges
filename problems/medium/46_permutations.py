from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtracking approach:
        # Build permutations by placing unused numbers at current position.
        n = len(nums)
        results: List[List[int]] = []
        if n == 0:
            return results  # Edge case: though problem constraints imply n >= 1
        used = [False] * n
        path = [0] * n

        def backtrack(pos: int) -> None:
            if pos == n:
                # A complete permutation is formed; store a shallow copy
                results.append(path[:])
                return
            # Try every unused number as the next element in the permutation
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path[pos] = nums[i]
                    backtrack(pos + 1)
                    # Backtrack: revert the choice
                    used[i] = False

        backtrack(0)
        return results