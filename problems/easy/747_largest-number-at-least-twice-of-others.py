class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        for i, val in enumerate(nums):
            if i == max_idx:
                continue
            if val * 2 > max_val:
                return -1
        return max_idx