from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Key insight: If we can form all sums in [1, miss-1], and we add a number x <= miss,
        # then we can form all sums in [1, miss + x - 1].
        # 
        # Strategy: Track the smallest sum we cannot yet form (miss).
        # - If current nums[i] <= miss, we can extend our range by adding nums[i]
        # - Otherwise, we must patch with 'miss' itself to optimally extend the range
        
        patches = 0  # Count of numbers we need to add
        miss = 1     # Smallest sum we cannot yet form
        i = 0        # Index in nums array
        
        # Continue until we can form all sums up to n
        while miss <= n:
            # If current number in nums can help extend our coverage
            if i < len(nums) and nums[i] <= miss:
                # By adding nums[i], we extend coverage from [1, miss-1] to [1, miss + nums[i] - 1]
                miss += nums[i]
                i += 1
            else:
                # nums[i] is too large or we've exhausted nums
                # Patch with 'miss' itself - this is optimal because:
                # - It extends coverage from [1, miss-1] to [1, 2*miss - 1]
                # - Any smaller patch would extend less; any larger would leave a gap
                patches += 1
                miss += miss  # Equivalent to miss *= 2
        
        return patches