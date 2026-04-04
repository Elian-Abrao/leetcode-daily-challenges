class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        # Impossible to see more sticks than exist, and at least one stick is always visible.
        if k < 1 or k > n:
            return 0

        # dp[j] = number of ways for the current stick count to have exactly j visible sticks.
        # We use 1D DP because each row depends only on the previous row.
        dp = [0] * (k + 1)
        dp[1] = 1  # With 1 stick, exactly 1 stick is visible.

        # Build answers from 2 sticks up to n sticks.
        for sticks in range(2, n + 1):
            # A configuration with more visible sticks than total sticks is impossible.
            upper_visible = min(sticks, k)

            # Iterate backwards so dp[j - 1] still represents the previous row.
            for visible in range(upper_visible, 0, -1):
                # Two ways to place the longest stick:
                # 1) Put it at the front -> it becomes visible, so we need visible-1 before it.
                # 2) Put it in any of the other (sticks - 1) positions -> it is hidden,
                #    and the visible count stays the same.
                dp[visible] = (
                    dp[visible - 1] + dp[visible] * (sticks - 1)
                ) % mod

            # Zero visible sticks is impossible for any positive number of sticks.
            dp[0] = 0

        return dp[k]