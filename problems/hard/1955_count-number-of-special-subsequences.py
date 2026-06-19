from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Dynamic programming approach:
        # dp[i] = number of valid subsequences ending at stage i
        # Stage 0: subsequences of only 0s (at least one)
        # Stage 1: subsequences of 0s followed by 1s (at least one of each)
        # Stage 2: subsequences of 0s, 1s, then 2s (at least one of each) - our answer
        
        # dp0: count of subsequences with only 0s
        # dp1: count of subsequences with 0s followed by 1s
        # dp2: count of subsequences with 0s, 1s, then 2s (complete special subsequences)
        dp0 = 0
        dp1 = 0
        dp2 = 0
        
        for num in nums:
            if num == 0:
                # We can either:
                # 1. Start a new subsequence with just this 0
                # 2. Append this 0 to any existing subsequence of 0s
                # Total ways = all existing dp0 subsequences extended + this new 0 alone
                # This is equivalent to: dp0_new = dp0 + dp0 + 1 = 2*dp0 + 1
                dp0 = (2 * dp0 + 1) % MOD
                
            elif num == 1:
                # We can either:
                # 1. Append this 1 to any existing subsequence ending in 0s (dp0 ways)
                # 2. Append this 1 to any existing subsequence ending in 1s (dp1 ways)
                # Total = dp0 + dp1 + dp1 = dp0 + 2*dp1
                dp1 = (dp0 + 2 * dp1) % MOD
                
            else:  # num == 2
                # We can either:
                # 1. Append this 2 to any existing subsequence ending in 1s (dp1 ways)
                # 2. Append this 2 to any existing complete subsequence (dp2 ways)
                # Total = dp1 + dp2 + dp2 = dp1 + 2*dp2
                dp2 = (dp1 + 2 * dp2) % MOD
        
        return dp2