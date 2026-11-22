from bisect import bisect_right

class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        """
        Each modulo class (indices i % k) forms an independent subsequence
        that must be made non-decreasing. Minimum changes per subsequence
        = length - len(longest non-decreasing subsequence).
        """
        n = len(arr)
        total_ops = 0

        # Process each remainder class separately
        for r in range(k):
            # Build the subsequence: arr[r], arr[r+k], arr[r+2k], ...
            sub = []
            i = r
            while i < n:
                sub.append(arr[i])
                i += k

            # Longest non-decreasing subsequence (LNDS) using patience sorting
            # tails[t] is the smallest possible tail value of a LNDS of length t+1
            tails = []
            for x in sub:
                # For non-decreasing we allow equal values -> bisect_right
                idx = bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x

            # Operations needed for this subsequence = total length - LNDS length
            total_ops += len(sub) - len(tails)

        return total_ops