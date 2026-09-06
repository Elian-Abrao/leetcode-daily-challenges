from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Returns True if there exists a subarray of length >= 2 whose sum
        is a multiple of k. Uses prefix sum modulo k.
        """
        # Map remainder -> first index where that remainder occurred.
        # Initialize with remainder 0 at index -1 (before any elements).
        remainder_first_occurrence = {0: -1}
        
        prefix_sum = 0
        for i, val in enumerate(nums):
            prefix_sum += val
            # Since k >= 1 by constraints, modulo is safe.
            remainder = prefix_sum % k
            
            if remainder in remainder_first_occurrence:
                # Found a previous index with same remainder.
                # If the subarray length is at least 2, it's valid.
                if i - remainder_first_occurrence[remainder] >= 2:
                    return True
            else:
                # Store the first occurrence of this remainder.
                remainder_first_occurrence[remainder] = i
        
        return False