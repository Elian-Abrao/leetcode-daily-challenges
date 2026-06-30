class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent by computing 1/x^|n|
        # This avoids complications with negative powers during recursion
        if n < 0:
            x = 1 / x
            n = -n
        
        # Use fast exponentiation (exponentiation by squaring)
        # Time complexity: O(log n) instead of O(n)
        # Space complexity: O(1) iterative approach
        result = 1.0
        current_product = x
        
        # Process each bit of the exponent
        # If bit i is set, multiply result by x^(2^i)
        while n > 0:
            # If current bit is 1, include current_product in result
            if n % 2 == 1:
                result *= current_product
            
            # Square the current product for next bit position
            # x -> x^2 -> x^4 -> x^8 -> ...
            current_product *= current_product
            
            # Move to next bit (right shift)
            n //= 2
        
        return result