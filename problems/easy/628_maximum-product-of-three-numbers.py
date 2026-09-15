from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array to easily access the smallest and largest numbers.
        # Key insight: maximum product can be either:
        # - product of the three largest numbers (all positive or mixed)
        # - product of the two smallest numbers (most negative) and the largest number
        #   (because product of two negatives yields a positive).
        nums.sort()
        # Candidate 1: product of three largest elements
        candidate1 = nums[-1] * nums[-2] * nums[-3]
        # Candidate 2: product of two smallest elements and the largest element
        candidate2 = nums[0] * nums[1] * nums[-1]
        # Return the larger of the two candidates
        return max(candidate1, candidate2)