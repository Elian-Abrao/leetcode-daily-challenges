class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        # dp[j] will store the LPS length for substring s[i..j] during the i-th iteration.
        dp = [0] * n

        # Iterate from the end of the string to the beginning.
        for i in range(n - 1, -1, -1):
            dp[i] = 1  # LPS length of a single character
            prev = 0   # stores dp[i+1][j-1] for the next j
            for j in range(i + 1, n):
                # Save current dp[j] before updating; it corresponds to dp[i+1][j]
                temp = dp[j]
                if s[i] == s[j]:
                    # Expand by 2 from the inner substring (i+1, j-1)
                    dp[j] = prev + 2
                else:
                    # Take max of dropping left character or right character
                    dp[j] = max(dp[j], dp[j - 1])
                # Update prev for the next j: the old dp[j] becomes dp[i+1][j] for the next iteration.
                prev = temp

        # After processing i=0, dp[n-1] holds the LPS length for the whole string.
        return dp[-1]