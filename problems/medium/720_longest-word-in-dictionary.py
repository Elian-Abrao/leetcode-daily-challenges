class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Set of "valid" words i.e. those whose every prefix is in the dictionary.
        # Empty string serves as the base for single‑character words.
        valid = {""}

        # Sorting lexicographically guarantees that any prefix of a word
        # is processed before the word itself (since a prefix is always
        # lexicographically smaller).
        words.sort()

        longest = ""
        for w in words:
            # A word can be built if its prefix (word without the last character)
            # is already valid. For length‑1 words this is the empty string.
            if w[:-1] in valid:
                valid.add(w)
                # Because we process in lexicographic order, the first valid word
                # of a given length is the lexicographically smallest among that length.
                if len(w) > len(longest):
                    longest = w

        return longest