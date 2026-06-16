from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Key insight: answer[i] = (product of all elements to the left of i) * (product of all elements to the right of i)
        # We can compute this in two passes without division:
        # 1. First pass: accumulate left products
        # 2. Second pass: accumulate right products and multiply with left products
        
        n = len(nums)
        answer = [1] * n
        
        # First pass: fill answer with left products
        # answer[i] will contain the product of all elements to the left of i
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Second pass: multiply by right products
        # We traverse from right to left, accumulating the product of elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer