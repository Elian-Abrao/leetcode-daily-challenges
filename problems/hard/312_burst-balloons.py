from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends to simplify boundary handling
        balloons = [1] + nums + [1]
        m = len(balloons)
        
        # dp[left][right] = max coins obtainable from bursting balloons strictly between indices left and right
        dp = [[0] * m for _ in range(m)]
        
        # Consider all possible interval lengths (distance between left and right)
        for length in range(2, m):  # at least one balloon between left and right
            for left in range(0, m - length):
                right = left + length
                best = 0
                left_val = balloons[left]
                right_val = balloons[right]
                # Iterate over the last balloon to burst in (left, right)
                for k in range(left + 1, right):
                    current = dp[left][k] + dp[k][right] + left_val * balloons[k] * right_val
                    if current > best:
                        best = current
                dp[left][right] = best
        
        return dp[0][m - 1]