from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Split both arrays into negatives, zeros, and positives.
        # The arrays are already sorted, so we can extract groups linearly.
        neg1 = [x for x in nums1 if x < 0]
        zero1_cnt = len([x for x in nums1 if x == 0])
        pos1 = [x for x in nums1 if x > 0]

        neg2 = [x for x in nums2 if x < 0]
        zero2_cnt = len([x for x in nums2 if x == 0])
        pos2 = [x for x in nums2 if x > 0]

        len_all1 = len(nums1)
        len_all2 = len(nums2)

        # For negative*negative products we need absolute values in increasing order.
        # The original negative parts are sorted ascending (e.g. -5, -3, -1).
        # Reversing and negating gives absolute values in ascending order (1, 3, 5).
        abs_neg1 = [-x for x in reversed(neg1)]
        abs_neg2 = [-x for x in reversed(neg2)]

        # --------------------------------------------------------------
        # Count how many pairs (i, j) have product <= `mid`.
        # --------------------------------------------------------------
        def count_leq(mid: int) -> int:
            total = 0

            # ---------- ZERO contributions ----------
            if mid >= 0:
                # All pairs where at least one element is zero produce product == 0,
                # which is <= mid when mid >= 0. Inclusion‑exclusion for double counting.
                total += zero1_cnt * len_all2 + zero2_cnt * len_all1 - zero1_cnt * zero2_cnt

            # ---------- POSITIVE * POSITIVE ----------
            # For each a in pos1 (increasing), we need b such that a*b <= mid.
            # Since pos2 is increasing, the condition is b <= mid // a.
            # As a grows, the bound decreases, so we can move a pointer from the right.
            j = len(pos2) - 1
            for a in pos1:
                limit = mid // a      # floor division, works for any mid
                while j >= 0 and pos2[j] > limit:
                    j -= 1
                if j < 0:
                    break
                total += j + 1

            # ---------- NEGATIVE * NEGATIVE (absolute values) ----------
            # Same logic as positive*positive, but using absolute values.
            j = len(abs_neg2) - 1
            for a in abs_neg1:
                limit = mid // a
                while j >= 0 and abs_neg2[j] > limit:
                    j -= 1
                if j < 0:
                    break
                total += j + 1

            # ---------- MIXED SIGNS (negative * positive) ----------
            if mid < 0:
                # Only negative‑positive pairs can be <= mid (they are negative).
                # Two cases: (neg1, pos2) and (pos1, neg2).

                # Case 1: neg1 * pos2
                # For each n in neg1 (ascending, e.g. -5, -3, -1),
                # need p in pos2 such that n * p <= mid.
                # Since n < 0, the inequality becomes p >= ceil(mid / n).
                # ceil(mid / n) = - (mid // abs(n))  (integer arithmetic).
                # As n increases (less negative), the threshold increases.
                # Walk pointer p_idx forward through pos2 (also increasing).
                p_idx = 0
                for n in neg1:
                    abs_n = -n
                    threshold = - (mid // abs_n)   # works because mid is negative
                    while p_idx < len(pos2) and pos2[p_idx] < threshold:
                        p_idx += 1
                    total += len(pos2) - p_idx

                # Case 2: pos1 * neg2
                # For each p in pos1 (increasing), need n in neg2 such that n * p <= mid.
                # Since p > 0, inequality becomes n <= floor(mid / p).
                # neg2 is sorted ascending (e.g. -5, -3, -1).
                # floor(mid / p) is negative and increases with p.
                # Walk pointer n_idx forward through neg2.
                n_idx = 0
                for p in pos1:
                    limit = mid // p      # floor, works for any mid
                    while n_idx < len(neg2) and neg2[n_idx] <= limit:
                        n_idx += 1
                    total += n_idx

            else:
                # mid >= 0: all negative‑positive pairs are ≤ 0 ≤ mid.
                total += len(neg1) * len(pos2) + len(pos1) * len(neg2)

            return total

        # --------------------------------------------------------------
        # Binary search over the possible product values.
        # --------------------------------------------------------------
        # Lower and upper bounds are the minimum and maximum possible products.
        # Because the arrays are sorted, the extremes come from the four corners.
        lo = min(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        )
        hi = max(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ) + 1   # exclusive upper bound

        # Standard binary search for the smallest product with count >= k.
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo