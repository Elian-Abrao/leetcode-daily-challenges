from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        In-place Dutch National Flag partitioning.
        - All 0s will be moved to the front.
        - All 1s will be in the middle.
        - All 2s will be moved to the end.
        Maintains invariants:
          0s in nums[0:low], 1s in nums[low:mid], 2s in nums[high+1:].
        """
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1