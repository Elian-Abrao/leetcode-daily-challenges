class Solution:
    def integerBreak(self, n: int) -> int:
        # Key insight: To maximize product, we should split n into parts that are as close to e ≈ 2.718
        # In integers, this means using 3s as much as possible, then 2s
        # Mathematical proof: for any integer >= 5, splitting into 3s gives better product than keeping it whole
        # For example: 6 = 3+3 -> 3*3=9 > 6; 5 = 3+2 -> 3*2=6 > 5
        
        # Edge cases: n=2 and n=3 must be handled specially because they must be split
        if n == 2:
            return 1  # 2 = 1 + 1, product = 1
        if n == 3:
            return 2  # 3 = 1 + 2, product = 2
        
        # For n >= 4, we use greedy approach: maximize number of 3s
        # Strategy:
        # - If n % 3 == 0: use all 3s
        # - If n % 3 == 1: use (n//3 - 1) threes and two 2s (because 3+3+3+1 < 3+3+2+2)
        # - If n % 3 == 2: use (n//3) threes and one 2
        
        product = 1
        
        # Keep breaking down n by subtracting 3s
        while n > 4:
            product *= 3
            n -= 3
        
        # At this point, n is 2, 3, or 4
        # Multiply the remaining part
        product *= n
        
        return product