class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Deduplicate: identical words can share the same encoding segment.
        word_set = set(words)
        # Remove every word that is a proper suffix of another word.
        # If w is a suffix of some longer word, w can be encoded implicitly
        # and does not need its own block.
        for w in list(word_set):          # iterate over a static copy
            for i in range(1, len(w)):    # every non‑empty proper suffix
                word_set.discard(w[i:])   # safe even if the suffix is absent
        # Each remaining word must appear as a separate block terminated by '#'.
        return sum(len(w) + 1 for w in word_set)