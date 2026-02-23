from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sorting to find the median; for even length, either middle value works
        nums.sort()
        mid = len(nums) // 2
        median = nums[mid]
        
        # Sum of moves equals total absolute deviation from the median
        moves = sum(abs(x - median) for x in nums)
        return moves