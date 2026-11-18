from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Build frequency counter for letters (case-insensitive)
        required = Counter()
        for ch in licensePlate:
            if ch.isalpha():
                required[ch.lower()] += 1

        # If no letters required, return the first word (all words are completing)
        if not required:
            return words[0]

        # Find the first letter in the license plate (case-insensitive)
        first_letter = None
        for ch in licensePlate:
            if ch.isalpha():
                first_letter = ch.lower()
                break

        first_comp = None
        best_word = None
        best_len = float('inf')

        # Scan words in order
        for word in words:
            # Optimization: skip words that can't be shorter than current best
            if len(word) >= best_len:
                continue

            # Check if word contains all required letters
            word_counts = Counter(word)
            is_completing = True
            for letter, needed in required.items():
                if word_counts[letter] < needed:
                    is_completing = False
                    break

            if is_completing:
                if first_comp is None:
                    first_comp = word
                if len(word) < best_len:
                    best_word = word
                    best_len = len(word)

        # Decision rule:
        # If the first completing word starts with the first letter of the license plate,
        # return it; otherwise return the shortest completing word.
        if first_comp and first_comp[0].lower() == first_letter:
            return first_comp
        else:
            return best_word