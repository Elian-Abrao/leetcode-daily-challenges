from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Strategy: Split into two 2-sum problems
        # - Compute all possible sums from nums1 and nums2, store in a hashmap
        # - For each sum from nums3 and nums4, check if its negative exists in the hashmap
        # Time: O(n^2), Space: O(n^2)
        
        # Build frequency map of all sums from first two arrays
        # Key: sum value, Value: count of ways to achieve that sum
        sum_map = defaultdict(int)
        
        # O(n^2): iterate all pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
        
        count = 0
        
        # O(n^2): iterate all pairs from nums3 and nums4
        for c in nums3:
            for d in nums4:
                # We need: a + b + c + d = 0
                # So: a + b = -(c + d)
                target = -(c + d)
                
                # If this target exists in sum_map, add its frequency to count
                # Each occurrence in sum_map represents a valid tuple
                if target in sum_map:
                    count += sum_map[target]
        
        return count