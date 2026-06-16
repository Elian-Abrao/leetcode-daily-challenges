class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes (due to the '-' sign)
        # Numbers ending in 0 are not palindromes (except 0 itself)
        # because leading zeros are not valid
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Special case: single digit numbers are always palindromes
        if x < 10:
            return True
        
        # Reverse half of the number and compare with the other half
        # This avoids potential overflow issues from reversing the entire number
        reversed_half = 0
        
        # Continue until we've processed half the digits
        # When reversed_half >= x, we've crossed the midpoint
        while x > reversed_half:
            # Extract last digit from x and append to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even-length numbers: x == reversed_half (e.g., 1221 -> 12 == 12)
        # For odd-length numbers: x == reversed_half // 10 (e.g., 12321 -> 12 == 123 // 10)
        # We discard the middle digit in odd-length case since it doesn't need comparison
        return x == reversed_half or x == reversed_half // 10