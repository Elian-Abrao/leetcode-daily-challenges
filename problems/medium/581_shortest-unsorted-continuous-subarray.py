from __future__ import annotations

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Find the leftmost index that is out of place
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:          # already sorted
            return 0

        # Find the rightmost index that is out of place
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find the minimum and maximum in the candidate subarray [left, right]
        min_val = min(nums[left:right+1])
        max_val = max(nums[left:right+1])

        # Extend left boundary if there is a greater element on the left,
        # or if the element is equal to min_val but the adjacent inner element is larger
        while left > 0 and (nums[left-1] > min_val or
                            (nums[left-1] == min_val and nums[left] > nums[left-1])):
            left -= 1

        # Extend right boundary if there is a smaller element on the right
        while right < n - 1 and nums[right+1] < max_val:
            right += 1

        return right - left + 1