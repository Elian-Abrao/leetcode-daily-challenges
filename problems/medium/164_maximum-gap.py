from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Edge case: less than 2 elements
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        # Edge case: all elements are the same
        if min_val == max_val:
            return 0
        
        # Bucket sort approach to achieve O(n) time complexity
        # Key insight: maximum gap must be at least ceiling((max - min) / (n - 1))
        # By using buckets of this size, the maximum gap will occur between buckets,
        # not within a bucket (pigeonhole principle)
        
        # Calculate bucket size (ceiling division)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Each bucket stores (min_value, max_value) for elements in that range
        # Using None to indicate empty buckets
        buckets = [[None, None] for _ in range(bucket_count)]
        
        # Distribute elements into buckets
        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            
            if buckets[bucket_idx][0] is None:
                # First element in this bucket
                buckets[bucket_idx][0] = num
                buckets[bucket_idx][1] = num
            else:
                # Update min and max for this bucket
                buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
                buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)
        
        # Find maximum gap by comparing max of previous non-empty bucket
        # with min of current non-empty bucket
        max_gap = 0
        prev_max = min_val  # Start with the global minimum
        
        for bucket in buckets:
            if bucket[0] is None:
                # Skip empty buckets
                continue
            
            # Gap is the difference between current bucket's min and previous bucket's max
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        
        return max_gap