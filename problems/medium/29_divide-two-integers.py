class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the only overflow case: -2^31 / -1 = 2^31 (exceeds INT_MAX)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        # Result is negative if signs differ
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values to simplify logic
        # Use abs() to avoid issues with INT_MIN (though we handle it above)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Use bit shifting to speed up division
        # Instead of subtracting divisor repeatedly (O(n)), we double divisor
        # and find largest multiple that fits, then repeat (O(log n * log n))
        while dividend >= divisor:
            # Find the largest multiple of divisor (as power of 2) that fits
            temp_divisor = divisor
            multiple = 1
            
            # Double temp_divisor until it exceeds dividend
            # Use bit shift to avoid multiplication: x << 1 == x * 2
            # Check (temp_divisor << 1) won't exceed dividend in next iteration
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple from dividend
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply sign to result
        if negative:
            quotient = -quotient
        
        # Clamp result to 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))