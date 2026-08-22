from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i, j = 0, 0
        sum1 = 0  # running sum for nums1 segment before next common element
        sum2 = 0  # running sum for nums2 segment before next common element
        result = 0

        # Two-pointer traversal: merge two sorted arrays, handling common elements
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # nums1 element is smaller, add to its segment sum
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                # nums2 element is smaller, add to its segment sum
                sum2 += nums2[j]
                j += 1
            else:
                # Common element: we can switch paths here
                # Choose the best accumulated sum from either array so far
                result = (result + max(sum1, sum2) + nums1[i]) % MOD
                # Reset segment sums for the next segment
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1

        # Add any remaining elements from either array (no more common elements)
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        # Final choice: take the better of the two remaining segments
        result = (result + max(sum1, sum2)) % MOD
        return result