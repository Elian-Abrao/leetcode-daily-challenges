from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # Count frequencies of each unique number in nums.
        freq_counts = list(Counter(nums).values())
        m = len(quantity)

        # Quick early exit: if total required items exceed total available items.
        if sum(quantity) > len(nums):
            return False

        # Precompute subset sums of quantity.
        # There are 2^m subsets, m <= 10, so at most 1024.
        subset_sum = [0] * (1 << m)
        for mask in range(1, 1 << m):
            # Get the lowest set bit to compute sum incrementally.
            lsb = mask & -mask
            idx = (lsb.bit_length() - 1)  # index of the bit
            prev = mask ^ lsb
            subset_sum[mask] = subset_sum[prev] + quantity[idx]

        # For each frequency, compute which subsets of customers can be satisfied.
        # We store a list of valid masks (subsets) for each frequency.
        freq_valid_masks = []
        for freq in freq_counts:
            masks = []  # 0 is always valid but we skip it for efficiency
            for mask in range(1, 1 << m):
                if subset_sum[mask] <= freq:
                    masks.append(mask)
            freq_valid_masks.append(masks)

        # DP over subsets of customers.
        # dp[mask] == True if the set of customers represented by 'mask' can be satisfied
        # using some subset of frequencies (each used at most once).
        dp = [False] * (1 << m)
        dp[0] = True

        # Process each frequency one by one.
        for masks in freq_valid_masks:
            # Copy current dp to avoid using the same frequency multiple times.
            new_dp = dp[:]  # shallow copy of boolean list is fine
            for mask in range(1 << m):
                if not dp[mask]:
                    continue
                # Try to add any subset that this frequency can satisfy.
                for submask in masks:
                    new_dp[mask | submask] = True
            dp = new_dp

        # The full set of all customers is mask (1<<m)-1.
        return dp[(1 << m) - 1]