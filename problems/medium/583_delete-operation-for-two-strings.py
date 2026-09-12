class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Minimum deletions to make word1 and word2 equal equals
        total length - 2 * LCS length.
        Compute LCS using O(min(m,n)) space DP.
        """
        n, m = len(word1), len(word2)
        # Optimize space: make word2 the shorter string
        if n < m:
            word1, word2 = word2, word1
            n, m = m, n

        # dp[j] = LCS length for processed prefix of word1 and word2[:j]
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0  # dp[i-1][j-1] for the current j
            for j in range(1, m + 1):
                # store current dp[j] before overwriting (becomes dp[i-1][j])
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp  # for next j, this becomes new prev

        lcs = dp[m]
        return (n + m) - 2 * lcs