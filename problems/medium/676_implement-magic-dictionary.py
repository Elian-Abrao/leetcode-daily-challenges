from __future__ import annotations

class MagicDictionary:
    """Data structure to check if changing exactly one character in a word
    yields a word from a given dictionary."""

    def __init__(self) -> None:
        # Map word length -> list of words of that length.
        self.words_by_len: dict[int, list[str]] = {}

    def buildDict(self, dictionary: list[str]) -> None:
        """Store the dictionary words grouped by length."""
        self.words_by_len.clear()  # reset (though only one call expected)
        for word in dictionary:
            length = len(word)
            # Append to the appropriate length group.
            if length not in self.words_by_len:
                self.words_by_len[length] = []
            self.words_by_len[length].append(word)

    def search(self, searchWord: str) -> bool:
        """Return True if exactly one character can be changed in searchWord
        to match any stored dictionary word."""
        n = len(searchWord)
        # Only words with the same length can possibly match.
        candidates = self.words_by_len.get(n)
        if not candidates:
            return False

        for word in candidates:
            diff = 0
            # Count differing characters.
            for i in range(n):
                if word[i] != searchWord[i]:
                    diff += 1
                    # If more than one difference, skip this word.
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False