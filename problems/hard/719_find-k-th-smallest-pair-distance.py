from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort array to enable binary search on distance and efficient counting
        nums.sort()
        n = len(nums)

        # Helper: count number of pairs (i<j) with distance <= d
        def count_pairs(d: int) -> int:
            count = 0
            # Two-pointer window: for each left index, expand right as far as possible
            right = 0
            for left in range(n):
                # Advance right while the pair distance stays within d
                while right < n and nums[right] - nums[left] <= d:
                    right += 1
                # All indices from left+1 up to right-1 form valid pairs with this left
                count += right - left - 1
            return count

        # Binary search over the answer (minimum distance such that count >= k)
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low