class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, no permutation can fit
        if len(s1) > len(s2):
            return False

        # Frequency counters for lowercase letters (26 letters)
        target = [0] * 26
        window = [0] * 26

        # Helper to convert character to index (0-25)
        def char_index(c: str) -> int:
            return ord(c) - ord('a')

        # Build frequency of s1 (target permutation)
        for ch in s1:
            target[char_index(ch)] += 1

        # Sliding window over s2
        n = len(s2)
        m = len(s1)
        for i in range(n):
            # Add current character to window
            window[char_index(s2[i])] += 1

            # Remove the character that falls out of the window
            if i >= m:
                window[char_index(s2[i - m])] -= 1

            # Compare window with target when window size equals m
            if i >= m - 1 and window == target:
                return True

        return False