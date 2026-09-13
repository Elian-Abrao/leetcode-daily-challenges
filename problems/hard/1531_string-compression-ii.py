class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        max_del = min(k, n)

        # rle_cost[length] = encoded length of a run of 'length' same characters.
        rle_cost = [0] * (n + 1)
        for length in range(1, n + 1):
            rle_cost[length] = 1 if length == 1 else 1 + len(str(length))

        INF = 10 ** 9

        # dp[i][d] = minimum compressed length for s[i:] using at most d deletions.
        dp = [[INF] * (max_del + 1) for _ in range(n + 1)]
        for d in range(max_del + 1):
            dp[n][d] = 0

        for i in range(n - 1, -1, -1):
            ch = s[i]
            for d in range(max_del + 1):
                # Option 1: delete s[i].
                best = dp[i + 1][d - 1] if d > 0 else INF

                # Option 2: keep s[i] and start a run of ch.
                # Try every possible final run length by scanning forward.
                seen = 0
                for j in range(i, n):
                    if s[j] != ch:
                        continue
                    seen += 1

                    # We keep the first 'seen' ch's in s[i..j].
                    # All other characters in this interval must be deleted.
                    removed = (j - i + 1) - seen
                    if removed <= d:
                        candidate = rle_cost[seen] + dp[j + 1][d - removed]
                        if candidate < best:
                            best = candidate

                dp[i][d] = best

        return dp[0][max_del]