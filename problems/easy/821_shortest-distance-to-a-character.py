class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        # Maximum possible distance is n-1, so initializing with n is safe.
        res = [n] * n

        # --- Left to right: distance to the nearest occurrence of c to the left ---
        prev = -n  # sentinel: no c seen yet
        for i, ch in enumerate(s):
            if ch == c:
                prev = i          # update the most recent c position
            res[i] = i - prev     # distance to previous c (could be large initially)

        # --- Right to left: consider nearest c to the right, keep the smaller ---
        nxt = 2 * n   # sentinel: no c seen yet when scanning backwards
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                nxt = i           # update the nearest c to the right
            # The minimal distance to any c is the smaller of the two passes
            res[i] = min(res[i], nxt - i)

        return res