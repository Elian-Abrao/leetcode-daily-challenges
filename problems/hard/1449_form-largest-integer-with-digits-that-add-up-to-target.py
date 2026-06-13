from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[i] = max number of digits achievable with cost exactly i
        # Initialize with -infinity to mark impossible states
        dp = [-float('inf')] * (target + 1)
        dp[0] = 0  # 0 cost = 0 digits
        
        # For each cost from 1 to target
        for i in range(1, target + 1):
            # Try using each digit (1-9)
            for digit in range(9):
                digit_cost = cost[digit]
                if digit_cost <= i:
                    # Can we use this digit and achieve cost i?
                    dp[i] = max(dp[i], dp[i - digit_cost] + 1)
        
        # If target cost is not achievable, return "0"
        if dp[target] < 0:
            return "0"
        
        # Reconstruct the largest number greedily
        result = []
        remaining = target
        
        # Greedily pick the largest digit that maintains max digit count
        for digit in range(9, 0, -1):  # Try digits 9 down to 1
            digit_cost = cost[digit - 1]  # digit maps to cost[digit-1]
            
            # Use this digit as many times as possible while maintaining optimality
            while remaining >= digit_cost and dp[remaining - digit_cost] == dp[remaining] - 1:
                result.append(str(digit))
                remaining -= digit_cost
        
        return ''.join(result)