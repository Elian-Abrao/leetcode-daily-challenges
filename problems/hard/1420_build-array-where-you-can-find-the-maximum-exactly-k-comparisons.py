class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # A non-empty array cannot have search cost 0.
        if k == 0:
            return 0

        # Search cost increases at most once per position and cannot exceed m
        # because each increase creates a new distinct maximum value.
        if k > n or k > m:
            return 0

        # dp[c][mx] = number of arrays for the current length
        # with search cost exactly c and final maximum exactly mx.
        dp = [[0] * (m + 1) for _ in range(k + 1)]

        # Length 1: choosing mx as the only element creates cost 1 in exactly one way.
        for mx in range(1, m + 1):
            dp[1][mx] = 1

        # Build arrays one position at a time.
        for length in range(2, n + 1):
            next_dp = [[0] * (m + 1) for _ in range(k + 1)]

            # Cost cannot exceed current length, so avoid useless work.
            max_cost = min(k, length)

            for cost in range(1, max_cost + 1):
                # Prefix sums let us query:
                # sum(dp[cost - 1][1..mx-1]) in O(1) per mx.
                prefix = 0

                for mx in range(1, m + 1):
                    # Option 1: append a value in [1..mx], so the maximum stays mx.
                    # There are exactly mx such choices.
                    ways_keep_max = dp[cost][mx] * mx

                    # Option 2: append the new maximum mx.
                    # Then the previous maximum must be smaller than mx,
                    # and the search cost increases by 1.
                    ways_make_new_max = prefix if cost > 1 else 0

                    next_dp[cost][mx] = (ways_keep_max + ways_make_new_max) % MOD

                    # Update prefix after using it so it represents maxima < next mx.
                    prefix += dp[cost - 1][mx]
                    if prefix >= MOD:
                        prefix -= MOD

            dp = next_dp

        # Sum over all possible final maxima.
        return sum(dp[k][1:]) % MOD