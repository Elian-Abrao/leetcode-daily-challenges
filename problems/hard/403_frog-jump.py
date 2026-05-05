from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Edge case: if second stone is not at position 1, impossible to start
        if len(stones) >= 2 and stones[1] != 1:
            return False
        
        # Convert stones list to set for O(1) lookup
        stone_set = set(stones)
        target = stones[-1]
        
        # Memoization: (current_position, last_jump) -> bool
        memo = {}
        
        def dfs(pos: int, k: int) -> bool:
            # Base case: reached the last stone
            if pos == target:
                return True
            
            # Check memo
            if (pos, k) in memo:
                return memo[(pos, k)]
            
            # Try all three possible next jumps: k-1, k, k+1
            for next_k in [k - 1, k, k + 1]:
                # Jump must be at least 1 unit
                if next_k <= 0:
                    continue
                
                next_pos = pos + next_k
                
                # Check if next position has a stone
                if next_pos in stone_set:
                    # Recursively check if we can reach the end from next_pos
                    if dfs(next_pos, next_k):
                        memo[(pos, k)] = True
                        return True
            
            # No valid path found from this state
            memo[(pos, k)] = False
            return False
        
        # Start at position 0 with initial jump of 1 (to reach position 1)
        return dfs(0, 0)