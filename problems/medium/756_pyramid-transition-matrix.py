from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build mapping from bottom pair (left, right) -> set of possible top colors
        # This allows O(1) lookup of valid tops for any adjacent pair
        pair_to_tops = defaultdict(set)
        for pattern in allowed:
            left, right, top = pattern[0], pattern[1], pattern[2]
            pair_to_tops[(left, right)].add(top)
        
        # Memoization cache to avoid recomputation for same state
        # Key: (tuple of current row characters) -> can we build from here?
        memo = {}
        
        def can_build(row: str) -> bool:
            """Returns True if we can build a pyramid starting from this row up to the top."""
            # Base case: single block at the top means we succeeded
            if len(row) == 1:
                return True
            
            # Check memo
            key = tuple(row)
            if key in memo:
                return memo[key]
            
            # Generate all possible next rows from current row
            # We need to consider every combination of valid tops for each adjacent pair
            # Use recursive DFS to explore all possibilities
            result = self._build_next(row, 0, "", pair_to_tops, memo)
            memo[key] = result
            return result
        
        return can_build(bottom)
    
    def _build_next(self, row: str, index: int, current_next: str, 
                    pair_to_tops: dict, memo: dict) -> bool:
        """
        Recursively try to build the next row above the current row.
        row: current level (string)
        index: position in row we are processing (0-based)
        current_next: partially built next row string
        Returns True if some complete next row can lead to a full pyramid.
        """
        # If we've processed all adjacent pairs in this row
        if index == len(row) - 1:
            # We have a complete next row; try to build from there
            return self._can_build_from_row(current_next, pair_to_tops, memo)
        
        # Get the pair of blocks at positions [index, index+1]
        left, right = row[index], row[index + 1]
        tops = pair_to_tops.get((left, right), set())
        
        # If no valid top exists for this pair, this path is dead
        if not tops:
            return False
        
        # Try each possible top block for this pair
        for top in tops:
            if self._build_next(row, index + 1, current_next + top, pair_to_tops, memo):
                return True
        
        return False
    
    def _can_build_from_row(self, row: str, pair_to_tops: dict, memo: dict) -> bool:
        """
        Helper to check if we can build a pyramid from a complete row.
        This avoids recursion depth issues by calling can_build via memo.
        """
        # Use memoized check for this row
        key = tuple(row)
        if key in memo:
            return memo[key]
        
        # Base case: single block at top
        if len(row) == 1:
            memo[key] = True
            return True
        
        # Recursively try to build next level
        result = self._build_next(row, 0, "", pair_to_tops, memo)
        memo[key] = result
        return result