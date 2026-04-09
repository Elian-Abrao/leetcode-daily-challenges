from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # With at most two transactions, track the best state after each action:
        # 1) first buy, 2) first sell, 3) second buy, 4) second sell.
        # This avoids O(n^2) splitting and stays O(n) time / O(1) space.
        if not prices:
            return 0

        # Use very small initial values for buy states because they represent profit
        # after spending money; starting from -price models buying on the first day.
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0

        for price in prices[1:]:
            # Either keep previous state or perform the action today.
            # Order matters: each state depends on the best earlier state from
            # the same iteration perspective, which this left-to-right update preserves.
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        # Doing nothing is always allowed, so sell states never drop below 0.
        return second_sell