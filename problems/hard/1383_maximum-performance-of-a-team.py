from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Key insight: For a given team, performance = sum(speeds) * min(efficiency)
        # Strategy: Sort engineers by efficiency (descending), then iterate considering
        # each engineer as the "minimum efficiency" of the team.
        # For each position, maintain the k-1 highest speeds seen so far.
        
        # Pair each engineer's efficiency with their speed, then sort by efficiency descending
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        # Min-heap to track the top k speeds (we'll remove smallest speeds when team size > k)
        min_heap = []
        speed_sum = 0
        max_performance = 0
        
        MOD = 10**9 + 7
        
        # Iterate through engineers in descending order of efficiency
        for eff, spd in engineers:
            # Add current engineer's speed to the team
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            
            # If team size exceeds k, remove the engineer with the smallest speed
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            
            # Calculate performance with current engineer as the minimum efficiency
            # (since we're iterating in descending efficiency order, current eff is the min)
            performance = speed_sum * eff
            
            # Track the maximum performance seen
            max_performance = max(max_performance, performance)
        
        return max_performance % MOD