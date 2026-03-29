from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []
        n = len(nums)

        def backtrack(start_index: int) -> None:
            # Once the current path is long enough, it is a valid answer.
            # We keep exploring because longer valid subsequences may exist.
            if len(path) >= 2:
                result.append(path[:])

            # Deduplicate choices only within this recursion depth.
            # This prevents generating the same subsequence from equal values
            # appearing at different positions.
            used_at_depth = set()

            for i in range(start_index, n):
                value = nums[i]

                # Enforce the non-decreasing property incrementally.
                if path and value < path[-1]:
                    continue

                # If this value was already tried at this depth, choosing it again
                # would produce duplicate subsequences with the same prefix.
                if value in used_at_depth:
                    continue

                used_at_depth.add(value)
                path.append(value)
                backtrack(i + 1)
                path.pop()

        # With n <= 15, exhaustive backtracking is feasible.
        # The pruning above keeps duplicates under control.
        backtrack(0)
        return result