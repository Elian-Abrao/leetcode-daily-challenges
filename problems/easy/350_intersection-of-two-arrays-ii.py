from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use Counter to track frequency of elements in both arrays
        # This allows us to handle duplicates correctly
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Result will contain elements present in both arrays
        # with frequency = min(freq in nums1, freq in nums2)
        result = []
        
        # Iterate through elements in the smaller counter for efficiency
        # For each common element, add it min(count1, count2) times
        for num in count1:
            if num in count2:
                # Add the minimum frequency of the element in both arrays
                min_count = min(count1[num], count2[num])
                result.extend([num] * min_count)
        
        return result