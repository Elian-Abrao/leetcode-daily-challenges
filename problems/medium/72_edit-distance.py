class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Let n be the shorter string length to keep memory at O(min(m, n)).
        # The DP relation only needs the previous row and the current row.
        if word1 == word2:
            return 0

        len1, len2 = len(word1), len(word2)

        # If one string is empty, every character of the other must be inserted/deleted.
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1

        # Use the shorter string as columns to reduce space usage.
        if len2 > len1:
            word1, word2 = word2, word1
            len1, len2 = len2, len1

        # prev[j] = edit distance between word1[:i-1] and word2[:j] for current i.
        prev = list(range(len2 + 1))

        for i in range(1, len1 + 1):
            # curr[0] means converting first i chars of word1 to empty string:
            # all i characters must be deleted.
            curr = [i] + [0] * len2
            char1 = word1[i - 1]

            for j in range(1, len2 + 1):
                char2 = word2[j - 1]

                if char1 == char2:
                    # Matching characters do not require a new operation.
                    curr[j] = prev[j - 1]
                else:
                    # Consider the three allowed operations:
                    # - delete from word1   -> prev[j]
                    # - insert into word1   -> curr[j - 1]
                    # - replace current char-> prev[j - 1]
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])

            prev = curr

        return prev[len2]