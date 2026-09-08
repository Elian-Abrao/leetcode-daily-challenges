from __future__ import annotations

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert integer to list of digits for easy manipulation
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the first digit from right that is smaller than its right neighbor
        # This is the pivot we need to increase to get a larger number
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        # If no such digit exists, digits are in descending order -> no larger permutation
        if i < 0:
            return -1
        
        # Step 2: Find the smallest digit to the right of i that is larger than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        # Step 3: Swap the pivot with this just-larger digit
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the suffix after i to get the smallest possible arrangement
        # The suffix was in descending order; reversing gives ascending order (minimum valid)
        left = i + 1
        right = length - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
        
        # Convert back to integer
        result = int(''.join(digits))
        
        # Check 32-bit integer constraint: maximum is 2^31 - 1 = 2147483647
        if result > 2**31 - 1:
            return -1
        
        return result