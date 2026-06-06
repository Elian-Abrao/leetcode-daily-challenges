from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[roll][last_digit][consecutive_count]
        # = number of ways to reach this state
        # roll: which roll we're on (0 to n-1)
        # last_digit: the last digit rolled (0-5 representing 1-6)
        # consecutive_count: how many times we've rolled last_digit consecutively (1 to rollMax[last_digit])
        
        # Initialize: for the first roll, we can roll any digit once
        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n + 1)]
        
        # Base case: after first roll, each digit appears once with count 1
        for digit in range(6):
            dp[1][digit][1] = 1
        
        # Fill the DP table for rolls 2 through n
        for roll in range(2, n + 1):
            for prev_digit in range(6):
                for prev_count in range(1, rollMax[prev_digit] + 1):
                    if dp[roll - 1][prev_digit][prev_count] == 0:
                        continue
                    
                    ways = dp[roll - 1][prev_digit][prev_count]
                    
                    # Try rolling each digit
                    for next_digit in range(6):
                        if next_digit == prev_digit:
                            # Continue the consecutive sequence
                            # Only allowed if we haven't hit the limit
                            if prev_count < rollMax[prev_digit]:
                                dp[roll][next_digit][prev_count + 1] = (
                                    dp[roll][next_digit][prev_count + 1] + ways
                                ) % MOD
                        else:
                            # Start a new consecutive sequence with count 1
                            dp[roll][next_digit][1] = (
                                dp[roll][next_digit][1] + ways
                            ) % MOD
        
        # Sum all valid ending states after n rolls
        result = 0
        for digit in range(6):
            for count in range(1, rollMax[digit] + 1):
                result = (result + dp[n][digit][count]) % MOD
        
        return result