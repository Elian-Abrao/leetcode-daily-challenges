class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)

        # Work with dyadic thresholds p / Q.  Q is chosen so that one step
        # (1/Q) is smaller than the minimum gap between two distinct fractions.
        max_val = arr[-1]
        Q = 1 << ((max_val * max_val).bit_length() + 1)

        def count_leq(p: int):
            """Return (count of fractions <= p/Q, largest such fraction)."""
            cnt = 0
            best_num, best_den = 0, 1
            j = 0

            for i in range(n - 1):
                # j must remain a valid denominator index: j > i.
                if j <= i:
                    j = i + 1

                # Find earliest denominator with arr[i]/arr[j] <= p/Q.
                while j < n and arr[i] * Q > p * arr[j]:
                    j += 1

                if j < n:
                    cnt += n - j
                    # For this numerator, the smallest valid denominator gives
                    # the largest fraction, so it is the only one worth tracking.
                    if best_num * arr[j] < arr[i] * best_den:
                        best_num, best_den = arr[i], arr[j]

            return cnt, best_num, best_den

        # Binary-search the first threshold with at least k fractions <= it.
        lo, hi = 0, Q
        while lo < hi:
            mid = (lo + hi) // 2
            cnt, _, _ = count_leq(mid)
            if cnt >= k:
                hi = mid
            else:
                lo = mid + 1

        # The largest fraction counted at this threshold is exactly the answer.
        _, num, den = count_leq(hi)
        return [num, den]