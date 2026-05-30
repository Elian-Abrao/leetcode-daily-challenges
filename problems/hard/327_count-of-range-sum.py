from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Use merge sort to count range sums efficiently
        # Key insight: For range sum S(i,j) = prefix[j] - prefix[i-1]
        # We need: lower <= prefix[j] - prefix[i-1] <= upper
        # Which means: prefix[j] - upper <= prefix[i-1] <= prefix[j] - lower
        
        # Build prefix sum array (with 0 at start for empty prefix)
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Use merge sort to count valid pairs while sorting
        def merge_sort_count(arr, start, end):
            # Base case: single element or empty
            if end - start <= 1:
                return 0
            
            mid = (start + end) // 2
            
            # Recursively count in left and right halves
            count = merge_sort_count(arr, start, mid) + merge_sort_count(arr, mid, end)
            
            # Count cross-boundary valid pairs
            # For each j in right half, find how many i in left half satisfy:
            # arr[j] - upper <= arr[i] <= arr[j] - lower
            
            # Use two pointers to find the range [left_ptr, right_ptr)
            # of elements in left half that satisfy the condition
            left_ptr = right_ptr = start
            
            for j in range(mid, end):
                # Find leftmost i where arr[i] >= arr[j] - upper
                while left_ptr < mid and arr[left_ptr] < arr[j] - upper:
                    left_ptr += 1
                
                # Find leftmost i where arr[i] > arr[j] - lower
                while right_ptr < mid and arr[right_ptr] <= arr[j] - lower:
                    right_ptr += 1
                
                # All elements in [left_ptr, right_ptr) form valid pairs with j
                count += right_ptr - left_ptr
            
            # Merge the two sorted halves
            merged = []
            i, j = start, mid
            while i < mid and j < end:
                if arr[i] <= arr[j]:
                    merged.append(arr[i])
                    i += 1
                else:
                    merged.append(arr[j])
                    j += 1
            
            # Add remaining elements
            merged.extend(arr[i:mid])
            merged.extend(arr[j:end])
            
            # Copy back to original array
            arr[start:end] = merged
            
            return count
        
        # Count valid range sums using merge sort on prefix sums
        return merge_sort_count(prefix, 0, len(prefix))