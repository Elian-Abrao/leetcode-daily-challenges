from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # Dynamic programming approach:
        # dp[i][j] = max value obtainable using first i piles and picking exactly j coins
        # For each pile, we can take 0 to min(len(pile), j) coins from the top
        
        n = len(piles)
        
        # Precompute prefix sums for each pile to quickly calculate sum of top t coins
        # prefix[i][t] = sum of first t coins from pile i
        prefix_sums = []
        for pile in piles:
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)
            prefix_sums.append(prefix)
        
        # dp[j] = max value with exactly j coins picked
        # We use 1D DP with space optimization (rolling array)
        dp = [0] * (k + 1)
        
        # Process each pile one by one
        for pile_idx in range(n):
            pile_size = len(piles[pile_idx])
            # Create new dp array for this iteration
            new_dp = dp[:]
            
            # For each possible total number of coins to pick
            for total_coins in range(k + 1):
                # Try taking 0 to min(pile_size, total_coins) coins from current pile
                # We need at least `take` coins available in total_coins
                max_take = min(pile_size, total_coins)
                
                for take in range(max_take + 1):
                    # If we take `take` coins from current pile:
                    # - We get prefix_sums[pile_idx][take] value
                    # - We need total_coins - take coins from previous piles
                    remaining = total_coins - take
                    value = dp[remaining] + prefix_sums[pile_idx][take]
                    new_dp[total_coins] = max(new_dp[total_coins], value)
            
            dp = new_dp
        
        return dp[k]