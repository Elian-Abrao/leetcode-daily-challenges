from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Quick edge-case: if p is longer than s, no anagrams possible
        m, n = len(p), len(s)
        if m > n:
            return []

        # We'll use simple fixed-size frequency arrays for lowercase letters.
        p_count = [0] * 26  # frequency of letters in p
        w_count = [0] * 26  # frequency of letters in current window of s
        a = ord('a')

        # Build frequency for p
        for ch in p:
            p_count[ord(ch) - a] += 1

        # Initialize the first window of length m with the first m characters of s
        for i in range(m):
            w_count[ord(s[i]) - a] += 1

        result = []
        # Check if the initial window is an anagram
        if w_count == p_count:
            result.append(0)

        # Slide the window across the rest of string s
        for i in range(m, n):
            # Add the new character entering the window
            w_count[ord(s[i]) - a] += 1
            # Remove the character leaving the window
            w_count[ord(s[i - m]) - a] -= 1

            # If current window matches p's frequency, record the start index
            if w_count == p_count:
                result.append(i - m + 1)

        return result