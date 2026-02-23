class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Helper: number of trailing zeros in x! is sum_{i>=1} floor(x / 5^i)
        def zero_count(x: int) -> int:
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        # Binary search for the smallest x such that f(x) >= k
        lo, hi = 0, 5 * (k + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if zero_count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        # If f(lo) == k, there are exactly 5 consecutive x's with that k
        return 5 if zero_count(lo) == k else 0