from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        # Edge case: empty or single price
        if n <= 1:
            return 0
        
        # If k >= n/2, we can do as many transactions as we want
        # This becomes the unlimited transactions problem
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                # Capture every positive price difference
                profit += max(0, prices[i] - prices[i-1])
            return profit
        
        # DP approach for limited transactions
        # buy[i][j] = max profit after at most i transactions with stock in hand on day j
        # sell[i][j] = max profit after at most i transactions with no stock on day j
        # We can optimize space by only keeping track of previous transaction state
        
        # buy[i] = max profit after completing i-th buy (holding stock after i-th transaction started)
        # sell[i] = max profit after completing i-th sell (not holding stock after i-th transaction completed)
        
        # Initialize: before any transactions, if we buy, we spend money
        buy = [-prices[0]] * (k + 1)
        sell = [0] * (k + 1)
        
        # Process each day
        for i in range(1, n):
            # We iterate transactions in reverse to avoid using updated values in same iteration
            for j in range(k, 0, -1):
                # sell[j]: either we already sold in transaction j, or we sell today
                # If we sell today, we must have bought in this transaction (buy[j])
                sell[j] = max(sell[j], buy[j] + prices[i])
                
                # buy[j]: either we already bought in transaction j, or we buy today
                # If we buy today, we must have completed j-1 transactions (sell[j-1])
                buy[j] = max(buy[j], sell[j-1] - prices[i])
        
        # Maximum profit after at most k transactions without holding stock
        return sell[k]