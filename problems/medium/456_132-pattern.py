from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # We need to find i < j < k where nums[i] < nums[k] < nums[j]
        # Strategy: traverse from right to left, maintaining:
        # - A stack of potential nums[j] candidates (decreasing order)
        # - The largest nums[k] found so far that is smaller than some nums[j] to its right
        
        # Edge case: need at least 3 elements for a 132 pattern
        if len(nums) < 3:
            return False
        
        stack = []  # Will store potential nums[j] values in decreasing order
        nums_k = float('-inf')  # The "3" in "132" - largest valid middle value found
        
        # Traverse from right to left
        # When we find nums[i] < nums_k, we have found a valid 132 pattern
        for i in range(len(nums) - 1, -1, -1):
            current = nums[i]
            
            # If current is less than nums_k, we found a 132 pattern
            # current is nums[i] (the "1"), nums_k is the "3", and some element in stack was the "2"
            if current < nums_k:
                return True
            
            # Update nums_k: pop elements smaller than current from stack
            # These popped elements become candidates for nums[k] (the "3" in 132)
            # We want the largest such element, so we keep updating nums_k
            while stack and stack[-1] < current:
                nums_k = stack.pop()
            
            # Push current onto stack as a potential nums[j] (the "2" in 132)
            # Stack maintains decreasing order from bottom to top
            stack.append(current)
        
        # No 132 pattern found
        return False