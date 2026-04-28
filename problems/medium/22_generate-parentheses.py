from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: we've used all n pairs of parentheses
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # We can add an open parenthesis if we haven't used all n yet
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # We can add a close parenthesis only if it doesn't exceed open ones
            # This ensures the parentheses remain well-formed at every step
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result