from typing import List
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # Key insight: With at most 200 blocked cells, the maximum area that can be
        # enclosed is roughly a triangle against a corner/edge of the grid.
        # Max enclosed area ≈ (200 * 199) / 2 ≈ 20,000 cells
        # If BFS from source explores more than this many cells without hitting target,
        # source is NOT trapped. Same logic applies for target.
        
        if not blocked:
            return True
        
        blocked_set = set(map(tuple, blocked))
        
        # Maximum area that can be enclosed by n blocked cells
        # For n blocks forming optimal barrier (triangle), area ≈ n*(n-1)/2
        max_blocked_area = len(blocked) * len(blocked) // 2
        
        def bfs(start, end):
            """
            BFS from start trying to reach end.
            Returns:
            - True if we reach end (definitely can reach)
            - True if we explore > max_blocked_area cells (not trapped, can escape)
            - False if trapped in a small region (explored < max_blocked_area and didn't reach end)
            """
            queue = deque([tuple(start)])
            visited = {tuple(start)}
            
            while queue and len(visited) <= max_blocked_area:
                x, y = queue.popleft()
                
                # If we reached the target, success
                if [x, y] == end:
                    return True
                
                # Explore 4 directions
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    
                    # Check boundaries
                    if 0 <= nx < 1000000 and 0 <= ny < 1000000:
                        if (nx, ny) not in visited and (nx, ny) not in blocked_set:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            
            # If we explored more than max_blocked_area cells, we escaped the enclosure
            return len(visited) > max_blocked_area
        
        # Check if source can escape or reach target
        # AND check if target can escape or reach source
        # Both must be true for a path to exist
        # The bidirectional check ensures neither source nor target is trapped
        return bfs(source, target) and bfs(target, source)