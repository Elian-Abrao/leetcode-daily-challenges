class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Ensure m is the smaller dimension to minimise the loop in count_leq
        if m > n:
            m, n = n, m

        def count_leq(x: int) -> int:
            """Return the number of multiplication table entries <= x."""
            total = 0
            # i is the row index (1‑based) up to m (the smaller dimension)
            # Because row i contributes min(n, x // i) entries.
            # Stop early when i > x because then x // i = 0.
            for i in range(1, m + 1):
                if i > x:
                    break
                total += min(n, x // i)
            return total

        # Binary search on the answer range [1, m*n]
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo