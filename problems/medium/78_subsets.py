from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Use backtracking to generate all subsets
        # Time: O(n * 2^n) - 2^n subsets, each requiring O(n) to copy
        # Space: O(n) recursion depth (excluding output array)
        
        result = []
        
        def backtrack(start: int, current: List[int]) -> None:
            # Add the current subset to result
            # Each call represents a valid subset at this decision point
            result.append(current[:])  # Make a copy to avoid mutation
            
            # Explore adding each remaining element
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current.append(nums[i])
                
                # Recurse with next index to avoid duplicates
                # start=i+1 ensures we only consider elements after current
                backtrack(i + 1, current)
                
                # Backtrack: remove the last added element
                current.pop()
        
        backtrack(0, [])
        return result