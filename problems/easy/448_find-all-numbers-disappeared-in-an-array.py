from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Strategy: Use the array itself as a hash table by marking visited indices
        # For each number x in nums, mark index (x-1) as visited by negating nums[x-1]
        # After one pass, any positive value at index i means (i+1) is missing
        
        # Time: O(n), Space: O(1) excluding output
        
        # First pass: mark presence by negating values at corresponding indices
        for num in nums:
            # Get the index corresponding to this number (convert 1-indexed to 0-indexed)
            index = abs(num) - 1
            
            # Skip if index is out of bounds (shouldn't happen with valid input)
            if index < 0 or index >= len(nums):
                continue
            
            # Mark this index as visited by making the value negative
            # Use abs() because the value might already be negative from a previous marking
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Second pass: collect all indices with positive values
        # These indices correspond to missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # Index i means number (i+1) is missing
                result.append(i + 1)
        
        return result