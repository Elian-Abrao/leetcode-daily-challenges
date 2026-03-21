from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count occurrences first; this is the core statistic we sort by.
        frequency = Counter(words)

        # Sort by:
        # 1) higher frequency first
        # 2) lexicographically smaller word first for ties
        # Using one global sort is both simple and fully correct here.
        ordered_words = sorted(frequency.keys(), key=lambda word: (-frequency[word], word))

        # k is guaranteed valid, so slicing is safe even for small unique counts.
        return ordered_words[:k]