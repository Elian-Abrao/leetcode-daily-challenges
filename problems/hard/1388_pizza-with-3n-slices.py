from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # This problem is equivalent to: pick n non-adjacent elements from a circular array
        # to maximize sum. When you pick a slice, the adjacent slices are removed (taken by Alice/Bob).
        # Since the array is circular, we can't pick both first and last element.
        # Solution: Solve twice - once excluding first element, once excluding last element.
        
        def maxSumNonAdjacent(arr: List[int], k: int) -> int:
            # DP: Pick k non-adjacent elements from linear array to maximize sum
            # dp[i][j] = max sum picking j elements from first i elements
            if not arr or k == 0:
                return 0
            
            n = len(arr)
            if k > (n + 1) // 2:  # Can't pick more than ceiling(n/2) non-adjacent elements
                return 0
            
            # dp[i][j] = max sum using first i elements and picking exactly j of them
            # We need i >= 2*j - 1 to have enough space for j non-adjacent picks
            dp = [[0] * (k + 1) for _ in range(n + 1)]
            
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    if j > (i + 1) // 2:
                        # Impossible to pick j non-adjacent from i elements
                        dp[i][j] = float('-inf')
                    else:
                        # Option 1: Don't pick element i-1
                        dp[i][j] = dp[i-1][j]
                        
                        # Option 2: Pick element i-1 (can't pick i-2, so use dp[i-2][j-1])
                        if i == 1:
                            dp[i][j] = max(dp[i][j], arr[i-1])
                        else:
                            dp[i][j] = max(dp[i][j], dp[i-2][j-1] + arr[i-1])
            
            return dp[n][k]
        
        n = len(slices) // 3  # We need to pick exactly n slices
        
        # Case 1: Exclude the last element (so we can potentially pick the first)
        case1 = maxSumNonAdjacent(slices[:-1], n)
        
        # Case 2: Exclude the first element (so we can potentially pick the last)
        case2 = maxSumNonAdjacent(slices[1:], n)
        
        # Return the maximum of both cases
        return max(case1, case2)