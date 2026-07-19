class Solution:
    def countDigitOne(self, n: int) -> int:
        # Edge case: if n is 0, no 1s appear
        if n <= 0:
            return 0
        
        # Digit DP approach: count 1s by analyzing each digit position
        # For each position (units, tens, hundreds, etc.), calculate how many times
        # digit 1 appears in that position across all numbers from 0 to n
        
        count = 0
        factor = 1  # Current position factor (1, 10, 100, 1000, ...)
        
        while factor <= n:
            # Split n into three parts relative to current position:
            # higher: digits above current position
            # cur: current digit
            # lower: digits below current position
            
            higher = n // (factor * 10)  # Digits to the left
            cur = (n // factor) % 10      # Current digit
            lower = n % factor            # Digits to the right
            
            # Count 1s at current position:
            # 1. From complete cycles of higher digits: higher * factor
            #    e.g., for n=2345, position=10s: hundreds digit can be 0,1,2
            #    When hundreds < 2, tens can be 0-9 and when it equals any of 0,1,
            #    the tens position can have 1 appear 10 times (0-9 in units)
            
            if cur == 0:
                # Current digit is 0: only complete cycles from higher digits contribute
                # e.g., n=2045, factor=10: 1 appears at tens place in 10-19, 110-119, ..., 1010-1019
                count += higher * factor
            elif cur == 1:
                # Current digit is 1: complete cycles + partial cycle up to lower
                # e.g., n=2145, factor=10: complete cycles + numbers 2140-2145 (6 numbers)
                count += higher * factor + lower + 1
            else:
                # Current digit > 1: complete cycles + one full cycle from current higher
                # e.g., n=2245, factor=10: includes 10-19, 110-119, ..., 2110-2119
                count += (higher + 1) * factor
            
            # Move to next digit position
            factor *= 10
        
        return count