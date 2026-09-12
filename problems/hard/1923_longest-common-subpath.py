from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # Edge case: no paths or empty path
        if not paths or not paths[0]:
            return 0

        # Determine the shortest and longest path lengths
        min_len = min(len(p) for p in paths)
        max_len = max(len(p) for p in paths)

        # If the shortest path is empty, no common subpath exists
        if min_len == 0:
            return 0

        # Rolling hash parameters (base > max possible city ID)
        BASE = 1000007          # prime > n (n <= 1e5)
        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009

        # Precompute powers of BASE up to max_len
        pow1 = [1] * (max_len + 1)
        pow2 = [1] * (max_len + 1)
        for i in range(1, max_len + 1):
            pow1[i] = (pow1[i - 1] * BASE) % MOD1
            pow2[i] = (pow2[i - 1] * BASE) % MOD2

        def get_hashes(arr: List[int], L: int) -> set:
            """
            Return a set of (hash1, hash2) tuples for every subarray of length L in arr.
            Uses double rolling hash to minimise collision probability.
            """
            if L == 0 or L > len(arr):
                return set()
            h1 = h2 = 0
            # Compute initial hash for the first L elements (shift values by 1 to avoid zero issues)
            for i in range(L):
                v = arr[i] + 1
                h1 = (h1 * BASE + v) % MOD1
                h2 = (h2 * BASE + v) % MOD2
            result = {(h1, h2)}
            # Use precomputed powers for efficient left-element removal
            powL1 = pow1[L - 1]
            powL2 = pow2[L - 1]
            for i in range(L, len(arr)):
                out_val = arr[i - L] + 1
                in_val  = arr[i] + 1
                # Remove the leftmost element
                h1 = (h1 - out_val * powL1) % MOD1
                h2 = (h2 - out_val * powL2) % MOD2
                # Shift window and add new element
                h1 = (h1 * BASE + in_val) % MOD1
                h2 = (h2 * BASE + in_val) % MOD2
                result.add((h1, h2))
            return result

        def can_form_common(L: int) -> bool:
            """Return True iff there exists a subarray of length L common to all paths."""
            if L == 0:
                return True
            if min_len < L:
                return False
            # Start with hashes from the first path
            common = get_hashes(paths[0], L)
            # Intersect with hashes from each subsequent path, early exit if empty
            for p in paths[1:]:
                if not common:
                    return False
                common &= get_hashes(p, L)
            return bool(common)

        # Binary search on the length of the common subpath
        low, high = 0, min_len  # inclusive high bound
        while low < high:
            mid = (low + high + 1) // 2  # upper‑mid to avoid infinite loop
            if can_form_common(mid):
                low = mid
            else:
                high = mid - 1
        return low