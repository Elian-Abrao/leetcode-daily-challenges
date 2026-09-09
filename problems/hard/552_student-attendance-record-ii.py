from __future__ import annotations

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[absences][consecutive_lates]
        # absences: 0 or 1
        # consecutive_lates: 0, 1, or 2 (cannot have 3 because that would be invalid)
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # empty record: 0 absences, 0 trailing L's

        for _ in range(n):
            # new state after adding one more day
            ndp = [[0] * 3 for _ in range(2)]

            for a in (0, 1):
                for l in (0, 1, 2):
                    cur = dp[a][l]
                    if cur == 0:
                        continue

                    # 1) Append 'P' (present): resets trailing L's, absences unchanged
                    ndp[a][0] = (ndp[a][0] + cur) % MOD

                    # 2) Append 'L' (late): allowed only if we haven't had 2 consecutive L's yet
                    if l < 2:
                        ndp[a][l + 1] = (ndp[a][l + 1] + cur) % MOD

                    # 3) Append 'A' (absent): allowed only if a == 0
                    if a == 0:
                        ndp[1][0] = (ndp[1][0] + cur) % MOD

            dp = ndp

        # Sum all valid states after n days
        total = 0
        for a in (0, 1):
            for l in (0, 1, 2):
                total = (total + dp[a][l]) % MOD
        return total