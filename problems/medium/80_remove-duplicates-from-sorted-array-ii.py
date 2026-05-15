from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: arrays with length <= 2 are already valid
        if len(nums) <= 2:
            return len(nums)
        
        # Two-pointer approach:
        # - `write_pos` marks where the next valid element should be written
        # - We iterate with `read_pos` through all elements
        # Key insight: element at write_pos can be written if it differs from
        # the element at write_pos - 2 (ensuring at most 2 duplicates)
        
        write_pos = 2  # First two elements are always valid
        
        for read_pos in range(2, len(nums)):
            # Allow current element if it's different from the element
            # two positions back in the result array
            # This guarantees each unique value appears at most twice
            if nums[read_pos] != nums[write_pos - 2]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos