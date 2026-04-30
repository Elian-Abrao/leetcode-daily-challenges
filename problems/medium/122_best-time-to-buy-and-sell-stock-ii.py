from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Key insight: Since we can buy and sell multiple times (even same day),
        # we can capture every upward price movement.
        # Simply sum all positive differences between consecutive days.
        # This is equivalent to buying at every local minimum and selling at every local maximum.
        
        # Edge case: empty or single element array
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        
        # Iterate through consecutive pairs of days
        for i in range(1, len(prices)):
            # If price goes up from day i-1 to day i, we capture that profit
            # This represents buying at i-1 and selling at i
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit