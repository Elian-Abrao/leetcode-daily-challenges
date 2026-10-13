class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        # Every local inversion is also a global inversion.
        # Equality holds iff there are no non-local global inversions.
        # For a permutation, this is equivalent to every element being
        # at most one position away from its sorted index.
        # Proof sketch: if nums[i] > i + 1, at least two smaller values
        # must appear after i; one may be at i+1, but the other creates
        # a non-local inversion. The symmetric argument covers nums[i] < i - 1.
        for i, val in enumerate(nums):
            if abs(val - i) > 1:
                return False
        return True