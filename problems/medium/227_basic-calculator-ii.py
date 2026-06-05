class Solution:
    def calculate(self, s: str) -> int:
        # Stack-based approach to handle operator precedence
        # * and / have higher precedence than + and -
        # We process operators immediately when they have high precedence
        # and defer + and - by pushing results to stack
        
        if not s:
            return 0
        
        stack = []
        current_number = 0
        operation = '+'  # Initialize with '+' to handle first number
        
        for i, char in enumerate(s):
            # Build multi-digit numbers
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # Process operator or end of string
            # We process when we hit an operator or reach the end
            # Skip spaces unless it's the last character
            if char in '+-*/' or i == len(s) - 1:
                if i == len(s) - 1 and char.isdigit():
                    # Ensure we process the last number
                    pass
                elif char == ' ' and i != len(s) - 1:
                    continue
                
                # Apply the previous operation to current_number
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    # High precedence: immediately apply to last stack value
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    # High precedence: immediately apply to last stack value
                    # Truncate toward zero for division
                    stack.append(int(stack.pop() / current_number))
                
                # Update operation for next iteration (only if current char is operator)
                if char in '+-*/':
                    operation = char
                
                # Reset current number for next operand
                current_number = 0
        
        # Sum all values in stack (handles deferred + and - operations)
        return sum(stack)