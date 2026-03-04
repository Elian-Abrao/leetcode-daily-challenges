class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick fail if lengths differ; they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Leverage the constraint: only lowercase English letters.
        # A fixed-size frequency array gives O(n) time and O(1) space.
        counts = [0] * 26
        base = ord('a')

        # Increment counts for characters in s.
        for ch in s:
            counts[ord(ch) - base] += 1

        # Decrement counts for characters in t.
        # If any count goes negative, t has more of some char than s -> not an anagram.
        for ch in t:
            idx = ord(ch) - base
            counts[idx] -= 1
            if counts[idx] < 0:
                return False

        return True