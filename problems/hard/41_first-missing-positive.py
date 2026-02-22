from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Place each number in its correct position if possible.
        # The correct position for value x (1 <= x <= n) is index x-1.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                # After swap, nums[i] could still be in [1..n], so re-check in next iteration

        # After placement, the first index i where nums[i] != i+1
        # indicates that value i+1 is missing.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions hold the correct values 1..n, the missing number is n+1.
        return n + 1