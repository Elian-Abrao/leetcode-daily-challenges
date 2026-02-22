from __future__ import annotations

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)

        # Build KMP LPS array for the evil string
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if evil[i] == evil[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Build transition table for automaton:
        # trans[state][c] gives the next matched-prefix-length of "evil"
        # after appending character c (0..25). If next_state == m, it means
        # we have matched the full evil string, which is invalid.
        trans = [[0] * 26 for _ in range(m)]
        for state in range(m):
            for c in range(26):
                ch = chr(97 + c)
                t = state
                # Follow failure links until we can extend the match with ch
                while t > 0 and evil[t] != ch:
                    t = lps[t - 1]
                if evil[t] == ch:
                    t += 1
                trans[state][c] = t

        # DP over positions with bounds and automaton state
        # dp[low][high][state] = number of ways for processed prefix
        # low: still equal to s1 so far (tight lower bound)
        # high: still equal to s2 so far (tight upper bound)
        # state: length of longest prefix of evil matched as suffix
        dp = [[[0] * m for _ in range(2)] for __ in range(2)]
        dp[1][1][0] = 1  # initially, we are tight to both s1 and s2, no evil matched

        for i in range(n):
            newdp = [[[0] * m for _ in range(2)] for __ in range(2)]
            loVal = ord(s1[i]) - 97
            hiVal = ord(s2[i]) - 97

            for low in (0, 1):
                for high in (0, 1):
                    for state in range(m):
                        val = dp[low][high][state]
                        if val == 0:
                            continue

                        min_c = loVal if low == 1 else 0
                        max_c = hiVal if high == 1 else 25

                        for c in range(min_c, max_c + 1):
                            next_state = trans[state][c]
                            if next_state == m:
                                # If evil is formed, skip this path
                                continue

                            next_low = 1 if (low == 1 and c == loVal) else 0
                            next_high = 1 if (high == 1 and c == hiVal) else 0

                            newdp[next_low][next_high][next_state] = (
                                newdp[next_low][next_high][next_state] + val
                            ) % MOD

            dp = newdp

        # Sum all possibilities after processing n characters
        ans = 0
        for low in (0, 1):
            for high in (0, 1):
                for state in range(m):
                    ans = (ans + dp[low][high][state]) % MOD

        return ans