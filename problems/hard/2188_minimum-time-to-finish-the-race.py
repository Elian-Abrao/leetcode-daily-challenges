from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # Maximum consecutive laps worth considering before changing
        # Beyond ~20 laps, exponential growth makes it always better to change
        # f * r^(x-1) grows very fast when r >= 2
        max_consecutive = 20
        
        # minCost[k] = minimum time to do k consecutive laps with any single tire
        # (without tire changes during these k laps)
        INF = float('inf')
        minCost = [INF] * (max_consecutive + 1)
        
        # For each tire, compute the cost of doing 1, 2, 3, ... consecutive laps
        for f, r in tires:
            total_time = 0
            lap_time = f
            
            for consecutive_laps in range(1, max_consecutive + 1):
                total_time += lap_time
                
                # Update the minimum cost for this many consecutive laps
                minCost[consecutive_laps] = min(minCost[consecutive_laps], total_time)
                
                # Next lap time with same tire
                lap_time *= r
                
                # Stop early if lap time becomes too large
                # (changeTime + f would be better than continuing)
                if lap_time > changeTime + f:
                    break
        
        # dp[i] = minimum time to complete exactly i laps
        dp = [INF] * (numLaps + 1)
        dp[0] = 0  # No time needed for 0 laps
        
        # For each number of laps
        for i in range(1, numLaps + 1):
            # Try all possible lengths for the last stint (consecutive laps without change)
            for last_stint in range(1, min(i, max_consecutive) + 1):
                # Cost = previous best + cost of last stint
                # If this isn't the first stint, add changeTime
                if i == last_stint:
                    # First stint, no change needed
                    dp[i] = min(dp[i], minCost[last_stint])
                else:
                    # Not first stint, need to change tire before this stint
                    dp[i] = min(dp[i], dp[i - last_stint] + changeTime + minCost[last_stint])
        
        return dp[numLaps]