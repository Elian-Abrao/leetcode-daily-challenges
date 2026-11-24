from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Maximize score by playing tokens face-up (spending power for score)
        or face-down (spending score for power).
        
        Key insight: Use a greedy two-pointer approach on sorted tokens.
        - Face-up: play smallest affordable token to gain score.
        - Face-down: sacrifice 1 score to get the largest token's power.
        
        Time: O(N log N) for sorting, O(N) for two-pointer traversal.
        Space: O(1) extra (excluding sort).
        """
        # Edge case: no tokens -> score stays 0
        if not tokens:
            return 0
        
        tokens.sort()
        n = len(tokens)
        
        # Two pointers: left for face-up (cheapest), right for face-down (most expensive)
        left = 0
        right = n - 1
        
        current_power = power
        score = 0
        max_score = 0  # Track max score ever achieved
        
        while left <= right:
            # Try to play the cheapest token face-up if we have enough power
            if current_power >= tokens[left]:
                current_power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            # If we have score to spare, trade the largest token for power
            elif score > 0:
                current_power += tokens[right]
                score -= 1
                right -= 1
            else:
                # Cannot make any more moves
                break
        
        return max_score