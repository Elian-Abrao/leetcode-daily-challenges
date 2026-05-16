from typing import List
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Key insight: A flower is in bloom at time t if start <= t <= end
        # Instead of checking each flower for each person, we use difference arrays
        # Track when flowers start blooming and when they stop
        
        # Extract and sort all start times
        starts = sorted([start for start, end in flowers])
        
        # Extract and sort all end times
        ends = sorted([end for start, end in flowers])
        
        # For each person at time t:
        # - Count flowers that have started by time t: bisect_right(starts, t)
        # - Count flowers that have ended before time t: bisect_left(ends, t)
        # - Flowers in bloom = started - ended
        
        # bisect_right(starts, t) gives count of flowers with start <= t
        # bisect_left(ends, t) gives count of flowers with end < t
        # So flowers in bloom = (flowers started) - (flowers already ended)
        
        result = []
        for person_time in people:
            # Count how many flowers have started blooming by person_time
            # bisect_right counts elements <= person_time
            started = bisect.bisect_right(starts, person_time)
            
            # Count how many flowers have finished blooming before person_time
            # bisect_left counts elements < person_time (since end is inclusive)
            ended = bisect.bisect_left(ends, person_time)
            
            # Flowers currently in bloom
            result.append(started - ended)
        
        return result