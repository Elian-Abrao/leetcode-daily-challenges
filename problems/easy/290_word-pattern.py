from __future__ import annotations

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the input string into words by spaces
        words = s.split()
        # The number of words must match the number of pattern letters
        if len(words) != len(pattern):
            return False

        # Establish bidirectional mappings: pattern char -> word, and word -> pattern char
        p2w = {}
        w2p = {}

        # Iterate in parallel over pattern and words
        for ch, word in zip(pattern, words):
            if ch in p2w:
                # If the existing mapping for this char doesn't match the current word, fail
                if p2w[ch] != word:
                    return False
            else:
                # If this word is already mapped to a different char, fail (bijective constraint)
                if word in w2p and w2p[word] != ch:
                    return False
                # Create the new bidirectional mapping
                p2w[ch] = word
                w2p[word] = ch

        # All checks passed; the string follows the given pattern
        return True