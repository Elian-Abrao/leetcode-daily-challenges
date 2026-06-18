from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Key insight: Process people from tallest to shortest.
        # When inserting a tall person, shorter people don't affect their count.
        # When inserting a shorter person, only previously inserted (taller) people matter.
        
        # Sort by height descending, then by k ascending
        # Descending height: process tallest first
        # Ascending k: among same height, smaller k should be placed first
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Build result by inserting each person at index k
        # Since we process tallest first, when we insert person [h, k],
        # all people already in queue have height >= h.
        # So inserting at position k ensures exactly k people in front with height >= h.
        result = []
        
        for person in people:
            # Insert person at index specified by their k value
            # This works because all previously inserted people are >= current height
            result.insert(person[1], person)
        
        return result