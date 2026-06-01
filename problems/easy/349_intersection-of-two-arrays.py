from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both arrays to sets to eliminate duplicates within each array
        # and enable O(1) average-case membership checks
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use set intersection operation to find common elements
        # This is efficient: O(min(len(set1), len(set2)))
        # Result is already unique since sets contain no duplicates
        return list(set1 & set2)