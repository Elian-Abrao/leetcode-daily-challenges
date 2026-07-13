from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen elements
        # This allows O(1) average-case lookup
        seen = set()
        
        for num in nums:
            # If we've already seen this number, we have a duplicate
            if num in seen:
                return True
            # Otherwise, add it to our seen set
            seen.add(num)
        
        # If we've processed all elements without finding duplicates
        return False
        
        # Alternative one-liner approach (equally efficient):
        # return len(nums) != len(set(nums))
        # 
        # Time complexity: O(n) where n is the length of nums
        # Space complexity: O(n) for the set in worst case (all unique elements)