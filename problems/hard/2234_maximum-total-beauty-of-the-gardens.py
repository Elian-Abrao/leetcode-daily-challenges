from __future__ import annotations
from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        
        # Count gardens already complete
        complete_idx = 0
        while complete_idx < n and flowers[complete_idx] >= target:
            complete_idx += 1
        
        # Gardens that are not complete
        incomplete = flowers[complete_idx:]
        m = len(incomplete)
        
        # Prefix sum for incomplete gardens
        prefix = [0] * (m + 1)
        for i in range(m):
            prefix[i+1] = prefix[i] + incomplete[i]
        
        best = 0
        
        # Try making different numbers of complete gardens from the incomplete ones
        # idx = how many incomplete gardens we decide to complete (starting from end)
        for complete_from_incomplete in range(m + 1):
            # Gardens that stay incomplete
            incomplete_count = m - complete_from_incomplete
            
            # Cost to complete the rightmost 'complete_from_incomplete' gardens
            cost_to_complete = 0
            for i in range(m - complete_from_incomplete, m):
                cost_to_complete += max(0, target - incomplete[i])
            
            if cost_to_complete > newFlowers:
                continue
            
            remaining = newFlowers - cost_to_complete
            
            # Current complete count includes already complete + newly completed
            total_complete = complete_idx + complete_from_incomplete
            
            if incomplete_count == 0:
                beauty = total_complete * full
                best = max(best, beauty)
                continue
            
            # We have incomplete_count gardens that can be improved
            # Binary search for maximum achievable minimum value
            lo = incomplete[0] if incomplete_count > 0 else 0
            hi = target - 1
            max_min = 0
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                # Find how many flowers needed to raise all incomplete to at least mid
                # Use binary search to find split point
                left, right = 0, incomplete_count
                while left < right:
                    mid_idx = (left + right) // 2
                    if incomplete[mid_idx] < mid:
                        left = mid_idx + 1
                    else:
                        right = mid_idx
                split = left
                
                needed = mid * split - prefix[split]
                
                if needed <= remaining:
                    max_min = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            beauty = total_complete * full + max_min * partial
            best = max(best, beauty)
        
        return best