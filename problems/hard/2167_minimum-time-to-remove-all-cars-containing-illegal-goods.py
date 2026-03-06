from __future__ import annotations

class Solution:
    def minimumTime(self, s: str) -> int:
        """
        Compute the minimum time to remove all '1's using:
        - remove from left end: 1 time unit per car
        - remove from right end: 1 time unit per car
        - remove any car from anywhere: 2 time units
        Strategy:
        - If we remove L prefix cars and R suffix cars, the remaining substring is s[L:n-R].
        - All '1's inside that substring can be removed for 2 each.
        - Time = L + R + 2 * count_ones_in(s[L:n-R]).
        - Reformulate to allow O(n) computation by dynamic precomputations.
        """
        n = len(s)
        # pref[i] = number of '1's in s[:i]
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (1 if ch == '1' else 0)

        # m[k] = -k + 2 * pref[k], for k in [0..n]
        # suff_min[L] = min_{k in [L..n]} m[k]
        m = [0] * (n + 1)
        for k in range(n + 1):
            m[k] = -k + 2 * pref[k]

        suff_min = [0] * (n + 1)
        cur_min = 10**18
        for k in range(n, -1, -1):
            if m[k] < cur_min:
                cur_min = m[k]
            suff_min[k] = cur_min

        # Evaluate minimal total time over all possible L
        # Time for given L is: (n + L - 2*pref[L]) + suff_min[L]
        # Explanation:
        # - c_L = n + L - 2*pref[L] comes from expanding the goal expression.
        # - suff_min[L] gives the best contribution from the right end decisions.
        ans = 10**18
        for L in range(n + 1):
            c_L = n + L - 2 * pref[L]
            cand = c_L + suff_min[L]
            if cand < ans:
                ans = cand

        return ans