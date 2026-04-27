class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Use a stack-based approach to track unmatched parentheses
        # Key idea: push indices onto stack, and when we find a valid pair,
        # we can compute the length of valid substring ending at current position
        
        # Edge case: empty string
        if not s:
            return 0
        
        # Stack stores indices of unmatched characters
        # Initialize with -1 as a base for calculating lengths
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push index of '(' onto stack
                stack.append(i)
            else:  # char == ')'
                # Pop the top element (could be matching '(' or previous base)
                stack.pop()
                
                if not stack:
                    # Stack is empty: current ')' has no match
                    # This becomes the new base for future valid substrings
                    stack.append(i)
                else:
                    # Valid pair found: calculate length from current top of stack
                    # The top of stack now points to the start boundary of valid substring
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
        
        return max_length