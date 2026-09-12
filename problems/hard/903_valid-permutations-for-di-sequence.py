class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # dp[j] = number of valid permutations of length i+1 ending with the j-th smallest number
        dp = [1]  # base case: only number 0
        for ch in s:
            m = len(dp)          # current length of dp (i+1)
            new_dp = [0] * (m + 1)
            # compute prefix sums of dp
            pref = [0] * m
            pref[0] = dp[0]
            for k in range(1, m):
                pref[k] = (pref[k-1] + dp[k]) % MOD
            total = pref[-1]  # sum of all dp values
            if ch == 'I':
                # new number must be larger than previous last => sum of dp[0..j-1]
                for j in range(m + 1):
                    new_dp[j] = pref[j-1] if j > 0 else 0
            else:  # 'D'
                # new number must be smaller than previous last => sum of dp[j..m-1]
                for j in range(m + 1):
                    # sum from j to m-1 inclusive = total - (pref[j-1] if j>0 else 0)
                    prev = pref[j-1] if j > 0 else 0
                    new_dp[j] = (total - prev) % MOD
            dp = new_dp
        return sum(dp) % MOD