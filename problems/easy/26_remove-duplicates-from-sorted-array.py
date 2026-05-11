from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: empty array should not occur per constraints, but handle single element
        if len(nums) <= 1:
            return len(nums)
        
        # Two-pointer approach:
        # 'write_pos' tracks where to write the next unique element
        # We iterate with 'i' to find unique elements
        write_pos = 1  # Start at index 1 since first element is always unique
        
        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # Since array is sorted, duplicates are adjacent
            # If current element differs from previous, it's unique
            if nums[i] != nums[i - 1]:
                # Place unique element at write_pos and advance
                nums[write_pos] = nums[i]
                write_pos += 1
        
        # write_pos now represents the count of unique elements
        # The first write_pos elements contain all unique values in sorted order
        return write_pos