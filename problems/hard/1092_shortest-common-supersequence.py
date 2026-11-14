class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        # dp[i][j] = length of shortest common supersequence for str1[:i] and str2[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base cases: supersequence with an empty string is the other string itself
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct the shortest supersequence from the dp table
        # Work backwards from (n, m) to (0, 0)
        i, j = n, m
        result = []

        while i > 0 or j > 0:
            if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
                # Characters match: take that character once
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif i > 0 and (j == 0 or dp[i - 1][j] <= dp[i][j - 1]):
                # Choose to take from str1 (gives shorter or equal supersequence)
                result.append(str1[i - 1])
                i -= 1
            else:
                # Take from str2
                result.append(str2[j - 1])
                j -= 1

        # The result was built from the end; reverse to get correct order
        return ''.join(reversed(result))