from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Edge case: if either array is empty, no pairs possible
        if not nums1 or not nums2:
            return []
        
        # Result list to store k smallest pairs
        result = []
        
        # Min-heap to always get the pair with smallest sum
        # Each entry: (sum, index_in_nums1, index_in_nums2)
        # We use the sum as the priority key
        heap = []
        
        # Initialize heap with pairs (nums1[i], nums2[0]) for all i
        # We only need to consider min(k, len(nums1)) starting pairs
        # because we need at most k pairs total
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract k smallest pairs
        while heap and len(result) < k:
            # Get the pair with smallest sum
            current_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # If there's a next element in nums2, push the pair (nums1[i], nums2[j+1])
            # This maintains the invariant that we explore pairs in increasing sum order
            # Key insight: for each i, we only advance j after popping (i, j)
            # This ensures we don't duplicate pairs and explore in optimal order
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result