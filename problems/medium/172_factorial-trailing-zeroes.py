class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Trailing zeros are produced by factors of 10 = 2 * 5
        # In n!, there are always more factors of 2 than 5
        # So we only need to count factors of 5
        
        # Count how many times 5 appears as a factor in n!
        # Numbers divisible by 5 contribute one factor of 5
        # Numbers divisible by 25 contribute an additional factor of 5
        # Numbers divisible by 125 contribute yet another factor of 5, etc.
        
        # Example: n = 30
        # 30/5 = 6 (numbers: 5, 10, 15, 20, 25, 30)
        # 30/25 = 1 (number: 25 contributes extra 5)
        # Total = 6 + 1 = 7 trailing zeros
        
        count = 0
        
        # Keep dividing n by powers of 5 and accumulate the count
        # This works in O(log_5(n)) time complexity
        while n >= 5:
            n //= 5
            count += n
        
        return count