class Solution:
    def calculate(self, s: str) -> int:
        # Stack-based approach to handle nested parentheses
        # We track the current result and sign, and push state when encountering '('
        
        stack = []  # Store (accumulated_result, sign_before_parenthesis) when entering '('
        result = 0  # Current accumulated result
        sign = 1    # Current sign: +1 for '+', -1 for '-'
        num = 0     # Current number being parsed
        
        for char in s:
            if char.isdigit():
                # Build multi-digit number
                num = num * 10 + int(char)
            
            elif char == '+':
                # Apply the accumulated number with its sign
                result += sign * num
                num = 0
                sign = 1  # Next number will be positive
            
            elif char == '-':
                # Apply the accumulated number with its sign
                result += sign * num
                num = 0
                sign = -1  # Next number will be negative
            
            elif char == '(':
                # Push current state to stack and reset for sub-expression
                # The sign before '(' affects everything inside the parentheses
                stack.append((result, sign))
                result = 0
                sign = 1
            
            elif char == ')':
                # Apply any remaining number in the sub-expression
                result += sign * num
                num = 0
                
                # Pop the state before this parenthesis
                prev_result, prev_sign = stack.pop()
                
                # Apply the sub-expression result with the sign before '('
                result = prev_result + prev_sign * result
            
            # else: skip spaces
        
        # Apply any remaining number (for expressions not ending with ')')
        result += sign * num
        
        return result