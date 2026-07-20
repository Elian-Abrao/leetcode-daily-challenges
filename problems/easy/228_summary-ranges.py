from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Edge case: empty array
        if not nums:
            return []
        
        result = []
        # Track the start of the current range
        start = 0
        
        # Iterate through array to find consecutive sequences
        for i in range(len(nums)):
            # Check if we're at the end OR next number is not consecutive
            # A break in sequence occurs when nums[i+1] != nums[i] + 1
            if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
                # Range found from start to i
                if start == i:
                    # Single element range
                    result.append(str(nums[start]))
                else:
                    # Multi-element range
                    result.append(f"{nums[start]}->{nums[i]}")
                
                # Move start to the next potential range
                start = i + 1
        
        return result