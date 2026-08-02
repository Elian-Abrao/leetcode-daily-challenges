from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Use merge sort with index tracking to count inversions
        # Each element needs to know how many smaller elements appear to its right
        # This is essentially counting inversions for each element
        
        n = len(nums)
        if n == 0:
            return []
        
        # Store (value, original_index) pairs to track positions during sort
        items = [(val, i) for i, val in enumerate(nums)]
        
        # Result array to store counts for each original index
        counts = [0] * n
        
        def merge_sort(arr):
            """
            Modified merge sort that counts smaller elements to the right.
            Returns sorted array by value while updating counts.
            """
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            # Merge phase: count how many elements from right are smaller
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    # When taking from left, all previously taken elements from right
                    # are smaller and to the right of this element in original array
                    counts[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    # Take from right (smaller element)
                    merged.append(right[j])
                    j += 1
            
            # Process remaining left elements
            while i < len(left):
                # All elements from right subarray have been taken (all are smaller)
                counts[left[i][1]] += j
                merged.append(left[i])
                i += 1
            
            # Process remaining right elements (no counts to update)
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(items)
        
        return counts