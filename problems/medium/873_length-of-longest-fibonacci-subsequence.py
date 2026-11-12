from __future__ import annotations
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Returns the length of the longest Fibonacci-like subsequence in the
        strictly increasing array arr. If none exists, returns 0.
        
        The core idea is dynamic programming on ordered pairs (i, j) with i < j.
        For each pair (i, j), we consider arr[i] and arr[j] as the first two
        elements of a Fibonacci-like sequence. The next element must be arr[k]
        = arr[i] + arr[j]. Since the array is strictly increasing, we can look
        up the index of arr[k] using a value-to-index map.
        
        We store dp[i][j] = length of the longest Fibonacci-like subsequence
        ending with (arr[i], arr[j]). The recurrence is:
            if arr[k] = arr[i] + arr[j] exists at index k:
                dp[j][k] = max(dp[j][k], dp[i][j] + 1)
        
        Time: O(n^2), Space: O(n^2) where n = len(arr) (max 1000, so ~1e6 pairs).
        """
        n = len(arr)
        # Map each value to its index for O(1) lookups.
        # Since arr is strictly increasing, values are unique.
        val_to_idx = {val: idx for idx, val in enumerate(arr)}
        
        # dp[i][j] = length of longest fib-like subsequence ending with arr[i], arr[j].
        # We'll store as list of dicts or 2D list. Use a 2D list initialized to 2
        # (since any pair of elements forms a base fib-like subsequence of length 2).
        dp = [[2] * n for _ in range(n)]
        
        best = 0  # Track the maximum length found (>=3 to be valid)
        
        # Iterate over the middle index j, then over the previous index i.
        # This order ensures that when we compute dp[i][j], all smaller pairs
        # (with smaller second index) have already been processed.
        for j in range(1, n):
            for i in range(j):
                # Compute the needed next value to extend the sequence.
                target = arr[i] + arr[j]
                
                # Important: target must be larger than arr[j] (since strictly increasing).
                # Also, the index k must exist in the array.
                if target > arr[-1]:  # Early skip: target exceeds max possible value.
                    continue
                
                k = val_to_idx.get(target, None)
                if k is not None and k > j:  # Ensure k comes after j for subsequence order.
                    # Extend the sequence ending with (i,j) by adding arr[k].
                    dp[j][k] = dp[i][j] + 1
                    best = max(best, dp[j][k])
        
        return best  # If no sequence of length >=3 found, best remains 0.