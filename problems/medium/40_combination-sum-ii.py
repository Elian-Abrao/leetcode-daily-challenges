from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort to enable pruning and duplicate handling
        candidates.sort()
        results: List[List[int]] = []
        path: List[int] = []
        n = len(candidates)

        def dfs(start: int, remaining: int) -> None:
            # If remaining is zero, we found a valid combination
            if remaining == 0:
                results.append(path.copy())
                return
            # Iterate through candidates starting from 'start'
            for i in range(start, n):
                current = candidates[i]
                # Since the list is sorted, no need to continue if current exceeds remaining
                if current > remaining:
                    break
                # Skip duplicates at the same recursion depth to avoid identical combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include current number and move to the next index (each number used at most once)
                path.append(current)
                dfs(i + 1, remaining - current)
                path.pop()

        dfs(0, target)
        return results