from __future__ import annotations
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array in ascending order using iterative merge sort.
        
        Achieves O(n log n) time complexity with O(n) auxiliary space.
        Uses a bottom-up (iterative) merge sort to avoid recursion overhead
        and stack overflow on large inputs (up to 5*10^4 elements).
        """
        # Handle edge cases: empty or single-element arrays are already sorted
        if not nums or len(nums) <= 1:
            return nums
        
        n = len(nums)
        # Temporary array for merging, reused to reduce allocations
        temp = [0] * n
        
        # width represents the size of subarrays being merged
        # Starts at 1 (single elements are trivially sorted)
        # Doubles each iteration until the whole array is sorted
        width = 1
        while width < n:
            # Process all pairs of subarrays of size 'width'
            left = 0
            while left < n:
                # Compute boundaries for the two subarrays to merge
                mid = left + width
                right = min(left + 2 * width, n)
                
                # Only merge if the second subarray has elements
                if mid < n:
                    # Merge nums[left:mid] and nums[mid:right] into temp
                    i, j, k = left, mid, left
                    left_end, right_end = mid, right
                    
                    while i < left_end and j < right_end:
                        if nums[i] <= nums[j]:
                            temp[k] = nums[i]
                            i += 1
                        else:
                            temp[k] = nums[j]
                            j += 1
                        k += 1
                    
                    # Copy remaining elements from left subarray
                    while i < left_end:
                        temp[k] = nums[i]
                        i += 1
                        k += 1
                    
                    # Copy remaining elements from right subarray
                    while j < right_end:
                        temp[k] = nums[j]
                        j += 1
                        k += 1
                    
                    # Copy merged result back to original array
                    nums[left:right] = temp[left:right]
                
                # Move to the next pair of subarrays
                left += 2 * width
            
            # Double the subarray size for next iteration
            width <<= 1
        
        return nums