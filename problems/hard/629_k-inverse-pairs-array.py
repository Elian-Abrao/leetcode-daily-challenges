class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j] = number of permutations of numbers processed so far
        # with exactly j inverse pairs.
        dp = [0] * (k + 1)
        dp[0] = 1  # empty permutation has 0 inversions

        # Iterate over numbers 1..n, building up the permutations.
        for i in range(1, n + 1):
            # new_dp will hold counts after inserting the number i.
            new_dp = [0] * (k + 1)
            # Maintain a sliding window sum of dp over at most i elements.
            window_sum = 0
            for j in range(k + 1):
                # Add dp[j] to the window (if within range).
                # The window corresponds to dp values for j, j-1, ..., j-(i-1).
                window_sum = (window_sum + dp[j]) % MOD
                # Remove the element that falls out of the window.
                if j - i >= 0:
                    window_sum = (window_sum - dp[j - i]) % MOD
                new_dp[j] = window_sum
            dp = new_dp

        return dp[k] % MOD