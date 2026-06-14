from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track the minimum price seen so far (best buying opportunity)
        min_price = float('inf')
        # Track the maximum profit achievable
        max_profit = 0
        
        # Single pass through prices: O(n) time, O(1) space
        for price in prices:
            # Update minimum price if current price is lower
            # This represents the best day to buy so far
            if price < min_price:
                min_price = price
            # Calculate profit if we sell at current price
            # (buying at the minimum price seen before today)
            else:
                profit = price - min_price
                # Update max profit if this transaction is better
                max_profit = max(max_profit, profit)
        
        # Return the best profit found, or 0 if no profitable transaction exists
        return max_profit