from __future__ import annotations
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Finds all common strings with the minimum index sum.
        """
        # Build a map from string to its index in list1
        index_map = {s: i for i, s in enumerate(list1)}
        
        min_sum = float('inf')       # smallest index sum found so far
        result: List[str] = []       # strings achieving the current min_sum
        
        # Scan list2 and check against the map
        for j, s in enumerate(list2):
            if s in index_map:
                total = index_map[s] + j
                if total < min_sum:
                    min_sum = total
                    result = [s]
                elif total == min_sum:
                    # Multiple common strings tie for the minimum sum
                    result.append(s)
        
        return result