from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """
        Returns the longest word from dictionary that is a subsequence of s.
        If multiple have the same length, pick the lexicographically smallest.
        """
        best = ""  # current best word (empty means none found)

        # Check each candidate word
        for word in dictionary:
            # Two-pointer subsequence check
            i = 0  # index in s
            j = 0  # index in word
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            # If we matched all characters, it's a valid subsequence
            if j == len(word):
                # Update best: longer length wins, or same length -> lexicographically smaller
                if (len(word) > len(best)) or (len(word) == len(best) and word < best):
                    best = word

        return best