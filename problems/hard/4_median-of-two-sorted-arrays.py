from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition nums1 at i (number of elements from nums1 in left half)
            i = (left + right) // 2
            # Partition nums2 at j (remaining elements needed for left half)
            j = half - i
            
            # Get boundary values around partitions
            # Use infinity for out-of-bounds to simplify comparisons
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            # Left half max should be <= right half min
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Correct partition found
                if total % 2 == 1:
                    # Odd total: median is the minimum of right half
                    return min(nums1_right, nums2_right)
                else:
                    # Even total: median is average of max(left) and min(right)
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                # nums1 partition is too far right, move left
                right = i - 1
            else:
                # nums1 partition is too far left, move right
                left = i + 1
        
        # Should never reach here with valid input
        return 0.0