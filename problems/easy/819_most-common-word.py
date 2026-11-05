import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Returns the most frequent word in the paragraph that is not in the banned list.
        Words are case-insensitive and punctuation is ignored.
        """
        # Normalize to lowercase and extract only alphabetic sequences (words)
        # Using [a-z]+ ensures we skip punctuation, spaces, and non-letter characters.
        words = re.findall(r'[a-z]+', paragraph.lower())
        
        # Convert banned list to a set for O(1) membership checks
        banned_set = set(banned)
        
        # Count frequencies, excluding banned words
        # Filter first to avoid counting banned words at all
        valid_words = [word for word in words if word not in banned_set]
        freq = Counter(valid_words)
        
        # Return the word with the highest frequency (guaranteed unique and non-empty)
        return max(freq, key=lambda w: freq[w])