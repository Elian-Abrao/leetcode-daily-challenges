from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Bucket sort approach: group numbers into buckets of size (valueDiff + 1)
        # If two numbers are in the same bucket, their difference is <= valueDiff
        # If they're in adjacent buckets, we need to check explicitly
        
        # Edge case: if valueDiff is 0 and indexDiff is large enough,
        # we're looking for exact duplicates within a window
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        # Bucket size: valueDiff + 1 ensures numbers in same bucket differ by <= valueDiff
        bucket_size = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            # Determine which bucket this number belongs to
            # Use floor division to handle negative numbers correctly
            bucket_id = num // bucket_size
            
            # Check if the same bucket already has a number (within indexDiff window)
            if bucket_id in buckets:
                return True
            
            # Check adjacent buckets (left and right)
            # Numbers in adjacent buckets might differ by <= valueDiff
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to its bucket
            buckets[bucket_id] = num
            
            # Maintain sliding window: remove the element that's now outside indexDiff range
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket_id = old_num // bucket_size
                del buckets[old_bucket_id]
        
        return False