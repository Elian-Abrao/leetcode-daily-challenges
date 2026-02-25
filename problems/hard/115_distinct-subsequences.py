class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # If t is empty, there is exactly one subsequence of s that matches it: the empty subsequence.
        if not t:
            return 1

        m = len(t)
        # dp[j] will hold the number of ways to form t[:j] using processed prefix of s.
        dp = [0] * (m + 1)
        dp[0] = 1  # empty t can always be formed

        # Process each character in s
        for ch in s:
            # Update dp from right to left to avoid reusing the same character multiple times
            for j in range(m, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        # Number of ways to form the entire t
        return dp[m]