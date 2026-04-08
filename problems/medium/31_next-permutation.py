from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # A single element already is both the highest and lowest permutation.
        if n <= 1:
            return

        # Find the first index from the right where the order increases.
        # Everything to the right of `pivot` is non-increasing, so it is the
        # largest suffix and must be adjusted to get the next permutation.
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        # If no pivot exists, the whole array is non-increasing, meaning we are
        # at the last permutation. Reversing gives the smallest permutation.
        if pivot == -1:
            nums.reverse()
            return

        # Find the rightmost element larger than the pivot value.
        # Using the rightmost valid choice keeps the increase minimal.
        successor = n - 1
        while nums[successor] <= nums[pivot]:
            successor -= 1

        # Swap pivot with the next larger value to make the permutation bigger.
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # Reverse the suffix because it is currently in descending order.
        # Reversing makes it the smallest possible suffix after the new prefix.
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1