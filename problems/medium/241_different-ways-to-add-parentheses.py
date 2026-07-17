from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Memoization to avoid recomputing same subexpressions
        memo = {}
        
        def compute(expr: str) -> List[int]:
            # Return cached result if available
            if expr in memo:
                return memo[expr]
            
            results = []
            
            # Try splitting at each operator
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Divide: split expression at this operator
                    left_part = expr[:i]
                    right_part = expr[i+1:]
                    
                    # Conquer: recursively compute all possible values for left and right
                    left_results = compute(left_part)
                    right_results = compute(right_part)
                    
                    # Combine: apply the operator to all combinations of left and right results
                    for left_val in left_results:
                        for right_val in right_results:
                            if char == '+':
                                results.append(left_val + right_val)
                            elif char == '-':
                                results.append(left_val - right_val)
                            elif char == '*':
                                results.append(left_val * right_val)
            
            # Base case: no operators found, expr is just a number
            if not results:
                results.append(int(expr))
            
            # Cache and return
            memo[expr] = results
            return results
        
        return compute(expression)