class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        """
        Returns a list of words that match the given pattern.
        A word matches the pattern if there exists a bijection (one-to-one mapping)
        between the letters of the pattern and the letters of the word.
        """
        # Length of pattern; all words have the same length per constraints.
        n = len(pattern)
        result = []

        for word in words:
            # Build mappings from pattern -> word and word -> pattern.
            # Using dictionaries to enforce bijection.
            p_to_w = {}
            w_to_p = {}
            matches = True

            for p_char, w_char in zip(pattern, word):
                # Check forward mapping: pattern char must map to the same word char.
                if p_char in p_to_w:
                    if p_to_w[p_char] != w_char:
                        matches = False
                        break
                else:
                    p_to_w[p_char] = w_char

                # Check reverse mapping: word char must map to the same pattern char.
                if w_char in w_to_p:
                    if w_to_p[w_char] != p_char:
                        matches = False
                        break
                else:
                    w_to_p[w_char] = p_char

            if matches:
                result.append(word)

        return result