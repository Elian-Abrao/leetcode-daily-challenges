class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # State machine approach:
        # cash = max profit on day i when NOT holding a stock
        # hold = max profit on day i when HOLDING a stock
        # 
        # On each day we have two options for each state:
        # - From cash: either do nothing (keep cash), or buy a stock (cash -> hold, pay price)
        # - From hold: either do nothing (keep hold), or sell the stock (hold -> cash, receive price, pay fee)
        
        # Initialize on day 0
        # Before any transactions, we have 0 cash and can't hold a stock unless we buy one
        cash = 0
        hold = -prices[0]  # buy on day 0, money spent
        
        for i in range(1, len(prices)):
            # Update cash: either keep previous cash, or sell today (from hold)
            new_cash = max(cash, hold + prices[i] - fee)
            
            # Update hold: either keep previous hold, or buy today (from cash)
            new_hold = max(hold, cash - prices[i])
            
            cash = new_cash
            hold = new_hold
        
        # At the end, we should prefer not holding a stock (sell to maximize profit)
        return cash