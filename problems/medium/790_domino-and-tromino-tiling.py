class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[state] after covering i columns (i = 0 initially)
        # state: 0 - no overhang,
        #        1 - top cell of next column already covered (overhang top)
        #        2 - bottom cell of next column already covered (overhang bottom)
        #        3 - both cells of next column already covered (overhang both)
        dp = [1, 0, 0, 0]   # empty board: only state 0 with 1 way

        for _ in range(n):
            nxt = [0] * 4

            # From state 0 (both cells of current column empty)
            nxt[0] = (nxt[0] + dp[0]) % MOD  # vertical domino -> no overhang
            nxt[1] = (nxt[1] + dp[0]) % MOD  # tromino covering both current + top next
            nxt[2] = (nxt[2] + dp[0]) % MOD  # tromino covering both current + bottom next
            nxt[3] = (nxt[3] + dp[0]) % MOD  # two horizontal dominos -> both next covered

            # From state 1 (top already filled, bottom empty)
            nxt[2] = (nxt[2] + dp[1]) % MOD  # horizontal domino covering bottom current+bottom next
            nxt[3] = (nxt[3] + dp[1]) % MOD  # tromino covering bottom current + both next

            # From state 2 (bottom already filled, top empty)
            nxt[1] = (nxt[1] + dp[2]) % MOD  # horizontal domino covering top current+top next
            nxt[3] = (nxt[3] + dp[2]) % MOD  # tromino covering top current + both next

            # From state 3 (both cells already filled by overhang)
            nxt[0] = (nxt[0] + dp[3]) % MOD  # no tile needed, move on with no overhang

            dp = nxt

        # A fully tiled board corresponds to state 0 after all columns
        return dp[0] % MOD