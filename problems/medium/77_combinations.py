from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate all possible combinations of k numbers from 1..n.
        Uses simple backtracking with increasing sequence to avoid duplicates.
        Time: O(C(n, k) * k), Space: O(k) for the current path plus O(C(n, k)) for results.
        """
        results: List[List[int]] = []
        
        # Quick edge-case handling; though per constraints k <= n and n >= 1
        if k <= 0 or n <= 0 or k > n:
            return results
        
        current: List[int] = []
        
        def backtrack(start: int) -> None:
            # If current combination is of size k, store a copy
            if len(current) == k:
                results.append(current.copy())
                return
            # Try adding each candidate number from 'start' to 'n'
            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1)  # Next number must be greater to maintain combination order
                current.pop()       # Backtrack

        backtrack(1)
        return results