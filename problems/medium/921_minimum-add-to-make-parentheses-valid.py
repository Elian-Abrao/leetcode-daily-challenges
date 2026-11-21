from __future__ import annotations

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Returns the minimum number of insertions needed to make the 
        parentheses string valid.
        
        Approach: Greedy counter with two tracking variables.
        - 'open_needed' tracks the net imbalance of opening parentheses.
        - 'close_needed' counts closing parentheses that lack a matching open.
        
        Time:  O(n) single pass
        Space: O(1) constant extra space
        """
        # Tracks unmatched opening parentheses that still need a closing ')'
        open_unmatched = 0
        # Tracks closing parentheses that appeared without a preceding '('
        close_unmatched = 0
        
        for ch in s:
            if ch == '(':
                # An opening parenthesis increases our need for a closing one
                open_unmatched += 1
            else:  # ch == ')'
                if open_unmatched > 0:
                    # This ')' matches a previous '('
                    open_unmatched -= 1
                else:
                    # No '(' to pair with this ')', we need to insert a '('
                    close_unmatched += 1
        
        # Total insertions = unmatched opens (need ')' each) + unmatched closes (need '(' each)
        return open_unmatched + close_unmatched