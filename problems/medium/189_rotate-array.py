from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Handle edge case: empty array or single element
        if n <= 1:
            return
        
        # Normalize k to avoid unnecessary full rotations
        # If k >= n, rotating n times brings us back to start
        k = k % n
        
        # If k is 0 after modulo, no rotation needed
        if k == 0:
            return
        
        # Use the reversal algorithm for O(1) space complexity:
        # 1. Reverse the entire array
        # 2. Reverse the first k elements
        # 3. Reverse the remaining n-k elements
        #
        # Example: nums = [1,2,3,4,5,6,7], k = 3
        # After step 1: [7,6,5,4,3,2,1]
        # After step 2: [5,6,7,4,3,2,1]
        # After step 3: [5,6,7,1,2,3,4]
        
        def reverse(left: int, right: int) -> None:
            """Helper function to reverse nums[left:right+1] in place."""
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Step 1: Reverse entire array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining n-k elements
        reverse(k, n - 1)