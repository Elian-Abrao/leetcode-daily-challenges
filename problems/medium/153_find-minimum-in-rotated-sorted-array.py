from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search approach to find minimum in O(log n) time
        # Key insight: In a rotated sorted array, one half is always sorted
        # The minimum is either at the rotation point or the first element
        
        left, right = 0, len(nums) - 1
        
        # If array is not rotated or has single element
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check if mid+1 is the minimum (rotation point)
            # This happens when mid element is greater than next element
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Check if mid is the minimum (rotation point)
            # This happens when mid element is less than previous element
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # Decide which half to search
            # If left half is sorted (nums[left] <= nums[mid]), 
            # the minimum must be in the right half
            if nums[left] <= nums[mid]:
                # Left half is sorted, minimum is in right half
                left = mid + 1
            else:
                # Right half is sorted, minimum is in left half
                right = mid
        
        # When left == right, we've found the minimum
        return nums[left]