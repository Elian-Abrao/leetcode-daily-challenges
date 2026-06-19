from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Track the smallest and second smallest values seen so far
        # These represent the first two elements of a potential triplet
        # Time: O(n), Space: O(1)
        
        # Initialize to infinity since we're looking for strictly increasing values
        first = float('inf')   # Smallest value seen
        second = float('inf')  # Second smallest value that comes after first
        
        for num in nums:
            # If we find a number smaller than or equal to first, update first
            # This gives us a better candidate for the start of the triplet
            if num <= first:
                first = num
            # If num > first but <= second, update second
            # Now we have a valid increasing pair (first, second)
            elif num <= second:
                second = num
            # If num > second, we have found our triplet: first < second < num
            # The indices satisfy i < j < k by construction (left-to-right scan)
            else:
                return True
        
        # No increasing triplet found
        return False