from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Precompute positions of each character in ring for O(1) lookup
        char_positions = {}
        for i, char in enumerate(ring):
            if char not in char_positions:
                char_positions[char] = []
            char_positions[char].append(i)
        
        n = len(ring)
        
        def min_distance(from_pos, to_pos):
            # Calculate minimum steps to rotate from from_pos to to_pos
            # Can go clockwise or counterclockwise
            clockwise = (to_pos - from_pos) % n
            counterclockwise = (from_pos - to_pos) % n
            return min(clockwise, counterclockwise)
        
        # DP with memoization: (key_index, current_ring_position) -> min steps
        @lru_cache(maxsize=None)
        def dp(key_idx, ring_pos):
            # Base case: finished spelling all characters in key
            if key_idx == len(key):
                return 0
            
            # Current character we need to spell
            target_char = key[key_idx]
            
            # Try all positions in ring where target_char appears
            min_steps = float('inf')
            for next_pos in char_positions[target_char]:
                # Cost to rotate from ring_pos to next_pos
                rotation_cost = min_distance(ring_pos, next_pos)
                # Cost to press button (always 1)
                press_cost = 1
                # Recursively find cost for remaining characters
                future_cost = dp(key_idx + 1, next_pos)
                
                total_cost = rotation_cost + press_cost + future_cost
                min_steps = min(min_steps, total_cost)
            
            return min_steps
        
        # Start at position 0 (12:00 direction), spelling from key[0]
        return dp(0, 0)