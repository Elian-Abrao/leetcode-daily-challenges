from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Binary search with modification for duplicates
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than rightmost, minimum must be in right half
            # Example: [3,4,5,1,2] where mid=5, right=2
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # If mid element is less than rightmost, minimum is in left half (including mid)
            # Example: [5,1,2,3,4] where mid=2, right=4
            elif nums[mid] < nums[right]:
                right = mid
            
            # If mid equals right, we can't determine which half has the minimum
            # Example: [2,2,2,0,2] - mid and right are both 2
            # We can safely exclude the rightmost element (duplicate exists at mid)
            # This degrades to O(n) in worst case (all equal elements)
            else:
                right -= 1
        
        # When left == right, we've found the minimum
        return nums[left]