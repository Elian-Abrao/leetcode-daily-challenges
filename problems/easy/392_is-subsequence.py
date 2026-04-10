class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Empty string is a subsequence of any string by definition.
        if not s:
            return True
        
        # If s is longer, it cannot fit as a subsequence.
        if len(s) > len(t):
            return False
        
        s_index = 0
        
        # Scan t once and greedily match the next needed character from s.
        # This is optimal here because preserving order is the only constraint.
        for char in t:
            if char == s[s_index]:
                s_index += 1
                
                # As soon as all characters in s are matched, we can stop early.
                if s_index == len(s):
                    return True
        
        # We exhausted t before matching every character in s.
        return False