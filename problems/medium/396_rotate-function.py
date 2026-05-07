from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Key insight: Instead of recalculating F(k) from scratch, derive F(k) from F(k-1)
        # 
        # For array [a, b, c, d]:
        # F(0) = 0*a + 1*b + 2*c + 3*d
        # F(1) = 0*d + 1*a + 2*b + 3*c  (rotate right by 1, or rotate left by n-1)
        #
        # Relationship between F(k) and F(k-1):
        # When we rotate right by 1:
        # - Last element moves to front (coefficient goes from (n-1) to 0, loses (n-1)*last)
        # - All other elements shift right (coefficients increase by 1, gain sum_except_last)
        # 
        # F(k) = F(k-1) + sum_of_all - n * nums[n-k]
        # where nums[n-k] is the element that moved from end to beginning
        
        n = len(nums)
        
        # Edge case: single element
        if n == 1:
            return 0
        
        # Calculate F(0) and sum of all elements
        total_sum = sum(nums)
        current_f = sum(i * nums[i] for i in range(n))
        
        # Track maximum value
        max_f = current_f
        
        # Calculate F(1), F(2), ..., F(n-1) using the recurrence relation
        # When rotating right by k positions, the element at index (n-k) moves to front
        for k in range(1, n):
            # Transition from F(k-1) to F(k)
            # Element at position (n-k) in original array moves from back to front
            # All other elements' indices increase by 1
            current_f = current_f + total_sum - n * nums[n - k]
            max_f = max(max_f, current_f)
        
        return max_f