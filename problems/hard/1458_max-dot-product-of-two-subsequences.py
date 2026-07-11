from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] represents the maximum dot product using 
        # subsequences from nums1[0:i] and nums2[0:j]
        # We initialize with -infinity to handle the "must be non-empty" constraint
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Iterate through all positions
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current product of nums1[i-1] and nums2[j-1]
                current_product = nums1[i-1] * nums2[j-1]
                
                # Option 1: Start a new subsequence with just this pair
                dp[i][j] = current_product
                
                # Option 2: Extend previous subsequence by adding this pair
                # Only valid if dp[i-1][j-1] represents a valid (non-empty) subsequence
                if dp[i-1][j-1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + current_product)
                
                # Option 3: Skip nums1[i-1] - use best result without it
                if dp[i-1][j] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                # Option 4: Skip nums2[j-1] - use best result without it
                if dp[i][j-1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[m][n]