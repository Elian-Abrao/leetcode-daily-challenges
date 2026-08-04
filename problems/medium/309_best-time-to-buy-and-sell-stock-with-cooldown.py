from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: can't make profit with 0 or 1 day
        if len(prices) <= 1:
            return 0
        
        # State machine DP approach
        # Three states to track at each day:
        # - hold: max profit if we hold a stock at end of day i
        # - sold: max profit if we just sold a stock on day i (enters cooldown next day)
        # - rest: max profit if we're resting (not holding, can buy tomorrow)
        
        # Initial states for day 0:
        # If we hold on day 0, we must have bought it
        hold = -prices[0]
        # Can't sell on day 0 (need to buy first)
        sold = 0
        # Starting with no action
        rest = 0
        
        # Process each subsequent day
        for i in range(1, len(prices)):
            price = prices[i]
            
            # Calculate new states based on previous day
            # New hold: either we already held, or we buy today (can only buy if we were resting)
            new_hold = max(hold, rest - price)
            
            # New sold: we sell today (can only sell if we were holding)
            new_sold = hold + price
            
            # New rest: either we were already resting, or we just finished cooldown from yesterday's sale
            new_rest = max(rest, sold)
            
            # Update states for next iteration
            hold = new_hold
            sold = new_sold
            rest = new_rest
        
        # At the end, we want max profit without holding stock
        # Best outcome is either we sold on last day or we're resting
        return max(sold, rest)