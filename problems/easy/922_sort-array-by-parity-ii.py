from __future__ import annotations

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """
        In-place rearrangement: place evens at even indices, odds at odd indices.
        Uses two-pointer swapping to achieve O(n) time and O(1) extra space.
        """
        n = len(nums)
        # Even pointer starts at index 0, odd pointer at index 1.
        even_idx = 0
        odd_idx = 1
        
        # Iterate until we've scanned all positions.
        # Even_idx moves by 2, so we only need to check one parity path.
        while even_idx < n and odd_idx < n:
            # If current even position already has an even number, move forward.
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            # If current odd position already has an odd number, move forward.
            elif nums[odd_idx] % 2 == 1:
                odd_idx += 2
            else:
                # Mismatch: even position has odd number, odd position has even number.
                # Swap them to fix both positions simultaneously.
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                even_idx += 2
                odd_idx += 2
        
        return nums