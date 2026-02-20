from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        n = len(nums)
        if n < 2 or indexDiff <= 0:
            return False

        w = valueDiff + 1  # bucket size
        buckets = {}

        for i, num in enumerate(nums):
            b = num // w
            # Check current bucket
            if b in buckets:
                return True
            # Check neighbor buckets
            left = b - 1
            right = b + 1
            if left in buckets and abs(num - buckets[left]) <= valueDiff:
                return True
            if right in buckets and abs(num - buckets[right]) <= valueDiff:
                return True
            # Insert current
            buckets[b] = num
            # Maintain window of size indexDiff
            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_b = old // w
                # Remove the old bucket entry
                if old_b in buckets:
                    del buckets[old_b]
        return False