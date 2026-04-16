from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Use in-place negative marking to detect duplicates.
        For each number x, mark the position x-1 as visited by negating nums[x-1].
        If we encounter a value whose target position is already negative,
        it means x has appeared before, hence it's a duplicate.
        This runs in O(n) time and uses O(1) extra space (aside from output).
        """
        res: List[int] = []
        n = len(nums)
        for i in range(n):
            # Map value to index (1-based to 0-based)
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                # Already visited -> this value is a duplicate
                res.append(idx + 1)
            else:
                # Mark as visited by negating the value at the derived index
                nums[idx] = -nums[idx]
        return res