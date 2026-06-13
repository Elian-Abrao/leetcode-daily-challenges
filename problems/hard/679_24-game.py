from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Use backtracking to try all possible combinations of operations and orderings
        # At each step, pick 2 numbers, apply an operation, and recurse with n-1 numbers
        # Base case: when we have 1 number left, check if it's close enough to 24
        
        def backtrack(nums):
            # Base case: if only one number remains, check if it equals 24
            # Use epsilon for floating point comparison due to division operations
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            # Try all pairs of numbers (i, j) where i < j
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    
                    # Create a new list with remaining numbers (excluding i and j)
                    remaining = []
                    for k in range(n):
                        if k != i and k != j:
                            remaining.append(nums[k])
                    
                    # Try all four operations between nums[i] and nums[j]
                    a, b = nums[i], nums[j]
                    
                    # Addition: commutative, so only try once per unordered pair
                    if backtrack(remaining + [a + b]):
                        return True
                    
                    # Subtraction: not commutative, order matters
                    if backtrack(remaining + [a - b]):
                        return True
                    
                    # Multiplication: commutative, so only try once per unordered pair
                    if backtrack(remaining + [a * b]):
                        return True
                    
                    # Division: not commutative, and need to avoid division by zero
                    if b != 0:
                        if backtrack(remaining + [a / b]):
                            return True
            
            return False
        
        # Convert cards to floats to handle division properly
        return backtrack([float(card) for card in cards])