class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Extract sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the integer digit by digit
        reversed_num = 0
        while x != 0:
            # Extract the last digit
            digit = x % 10
            x //= 10
            
            # Check for overflow before actually adding the digit
            # If reversed_num > INT_MAX // 10, then reversed_num * 10 will overflow
            # If reversed_num == INT_MAX // 10, check if adding digit causes overflow
            if reversed_num > INT_MAX // 10:
                return 0
            if reversed_num == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0
            
            # Build the reversed number
            reversed_num = reversed_num * 10 + digit
        
        # Apply the original sign
        result = sign * reversed_num
        
        # Final boundary check (though the loop should have caught overflow)
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result