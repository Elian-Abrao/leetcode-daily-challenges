from __future__ import annotations

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # Edge case: if s1 is empty, we can't form any s2
        if not s1 or not s2:
            return 0
        
        # We need to find how many times we can form [s2, n2] from [s1, n1]
        # Strategy: iterate through copies of s1 and track how many s2's we complete
        # Use cycle detection to avoid iterating through all n1 copies
        
        # Map: (current position in s2) -> (count of s1 used, count of s2 completed)
        seen = {}
        s1_count = 0  # How many s1's we've processed
        s2_count = 0  # How many s2's we've completed
        s2_idx = 0    # Current position in s2 we're trying to match
        
        # Process copies of s1 until we either finish all n1 or find a cycle
        while s1_count < n1:
            # Check if we've seen this s2_idx at the start of processing an s1 before
            if s2_idx in seen:
                # Cycle detected! We can skip ahead
                prev_s1_count, prev_s2_count = seen[s2_idx]
                
                # How many s1's and s2's in one cycle
                cycle_s1_len = s1_count - prev_s1_count
                cycle_s2_len = s2_count - prev_s2_count
                
                # How many complete cycles can we fit in remaining s1's
                remaining_s1 = n1 - s1_count
                complete_cycles = remaining_s1 // cycle_s1_len
                
                # Skip ahead by complete cycles
                s1_count += complete_cycles * cycle_s1_len
                s2_count += complete_cycles * cycle_s2_len
                
                # Clear the seen map since we've fast-forwarded
                seen = {}
                
                # If we've reached exactly n1, we're done
                if s1_count == n1:
                    break
            
            # Record state before processing this s1
            seen[s2_idx] = (s1_count, s2_count)
            
            # Process one copy of s1, trying to match characters in s2
            for char in s1:
                if char == s2[s2_idx]:
                    s2_idx += 1
                    # If we completed one s2, reset index and increment count
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
            
            s1_count += 1
        
        # We've completed s2_count copies of s2
        # Each valid result needs n2 copies of s2
        return s2_count // n2