from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        if m > n:
            return 0

        if len(set(words)) == 1 and len(set(words[0])) == 1 and len(set(target)) == 1 and words[0][0] == target[0]:
            return pow(len(words), m, MOD)

        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for pos, ch in enumerate(word):
                freq[pos][ord(ch) - 97] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            need = ord(target[i - 1]) - 97
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if freq[j - 1][need] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * freq[j - 1][need]) % MOD

        return dp[m][n]