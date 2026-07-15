class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Use a monotonic increasing stack to build the smallest number
        # Strategy: remove digits when we find a smaller digit that can replace a larger one
        
        stack = []
        removals_left = k
        
        for digit in num:
            # Remove larger digits from stack while we can still remove digits
            # and current digit is smaller than the top of stack
            # This ensures we keep the smallest possible digits in their positions
            while stack and removals_left > 0 and stack[-1] > digit:
                stack.pop()
                removals_left -= 1
            
            stack.append(digit)
        
        # If we haven't removed k digits yet (happens when num is non-decreasing)
        # remove from the end since those are the largest
        if removals_left > 0:
            stack = stack[:-removals_left]
        
        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Edge case: if result is empty (all digits removed or all were zeros), return "0"
        return result if result else '0'