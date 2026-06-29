from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Edge case: empty attack series
        if not timeSeries:
            return 0
        
        total_poisoned = 0
        
        # Iterate through each attack timestamp
        for i in range(len(timeSeries)):
            if i == len(timeSeries) - 1:
                # Last attack: always contributes full duration
                total_poisoned += duration
            else:
                # Calculate time gap between current and next attack
                gap = timeSeries[i + 1] - timeSeries[i]
                
                # If gap >= duration, full duration is added (no overlap)
                # If gap < duration, only the gap is added (poison resets before expiring)
                total_poisoned += min(gap, duration)
        
        return total_poisoned