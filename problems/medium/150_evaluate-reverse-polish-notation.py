from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to evaluate RPN expression
        # Push operands onto stack, pop two operands when operator is encountered
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Pop two operands (order matters for - and /)
                # Second operand is popped first, first operand is popped second
                b = stack.pop()
                a = stack.pop()
                
                # Apply the operator and push result back
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # token == '/'
                    # Truncate toward zero: int(a/b) works for positive results
                    # but for negative results, Python's // floors towards negative infinity
                    # so we use int(a/b) which truncates toward zero as required
                    result = int(a / b)
                
                stack.append(result)
            else:
                # Token is an operand (possibly negative), convert to int and push
                stack.append(int(token))
        
        # Final result is the only element left in stack
        return stack[0]