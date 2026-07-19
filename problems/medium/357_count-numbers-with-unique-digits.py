class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Edge case: n = 0 means range [0, 1), only 0 is valid
        if n == 0:
            return 1
        
        # Edge case: n > 10 is impossible to have all unique digits
        # since we only have 10 distinct digits (0-9)
        # But constraint says n <= 8, so we handle up to n = 10 for robustness
        if n > 10:
            n = 10
        
        # Start with all 1-digit numbers: 0-9 (10 numbers)
        total = 10
        
        # For numbers with exactly k digits (k >= 2):
        # - First digit: 9 choices (1-9, can't be 0)
        # - Second digit: 9 choices (0-9 except the first digit)
        # - Third digit: 8 choices (0-9 except first two)
        # - ...
        # - k-th digit: (11 - k) choices
        
        # unique_count tracks numbers with exactly k unique digits
        unique_count = 9  # Start with 9 for 2-digit numbers (first digit choice)
        available_digits = 9  # Remaining choices for subsequent positions
        
        # Iterate from 2-digit numbers up to n-digit numbers
        for k in range(2, n + 1):
            unique_count *= available_digits
            total += unique_count
            available_digits -= 1
            
            # Stop early if no more unique digits possible
            if available_digits == 0:
                break
        
        return total