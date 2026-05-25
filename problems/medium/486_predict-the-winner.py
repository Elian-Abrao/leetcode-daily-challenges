from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Dynamic programming approach where we track the maximum score difference
        # a player can achieve over their opponent in a subarray [i, j]
        
        n = len(nums)
        
        # dp[i][j] = max score difference (current player - opponent) 
        # when playing optimally on subarray nums[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single element subarrays
        # When there's only one element, current player takes it, opponent gets 0
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Fill the DP table for increasing subarray lengths
        # We build from smaller subarrays to larger ones
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Current player can choose either nums[i] or nums[j]
                # If they choose nums[i]:
                #   - They gain nums[i]
                #   - Opponent plays optimally on [i+1, j] and gets dp[i+1][j]
                #   - Current player's advantage = nums[i] - dp[i+1][j]
                take_left = nums[i] - dp[i + 1][j]
                
                # If they choose nums[j]:
                #   - They gain nums[j]
                #   - Opponent plays optimally on [i, j-1] and gets dp[i][j-1]
                #   - Current player's advantage = nums[j] - dp[i][j-1]
                take_right = nums[j] - dp[i][j - 1]
                
                # Choose the maximum advantage
                dp[i][j] = max(take_left, take_right)
        
        # Player 1 wins if their score difference is non-negative
        # (since ties go to Player 1)
        return dp[0][n - 1] >= 0