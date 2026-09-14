from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Use index marking technique to detect duplicates
        # Mark an index as visited by making its value negative
        duplicate = -1
        for num in nums:
            index = abs(num) - 1  # convert 1-based to 0-based index
            if nums[index] < 0:
                # This number is a duplicate because we've already marked it
                duplicate = abs(num)
            else:
                nums[index] = -nums[index]
        
        # Find the missing number (the index with positive value)
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1  # convert back to 1-based
                break
        
        return [duplicate, missing]