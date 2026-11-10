from __future__ import annotations

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # Count word frequencies across both sentences using a single dictionary.
        # A word is "uncommon" if its total count across both sentences is exactly 1.
        # This captures both cases: appears once in one sentence and zero in the other.
        freq: dict[str, int] = {}
        
        # Process both sentences: split by spaces since words are single-space separated.
        for word in s1.split():
            freq[word] = freq.get(word, 0) + 1
        for word in s2.split():
            freq[word] = freq.get(word, 0) + 1
        
        # Collect words that appear exactly once overall.
        return [word for word, count in freq.items() if count == 1]