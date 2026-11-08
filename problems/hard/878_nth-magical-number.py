class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        # Compute least common multiple of a and b.
        # Using math.gcd is fine; no need for math.lcm (Python 3.9+).
        import math
        lcm = a // math.gcd(a, b) * b  # Prevent overflow by dividing first.

        # Count of magical numbers up to x:
        # Numbers divisible by a (x//a) plus numbers divisible by b (x//b)
        # minus those counted twice (divisible by lcm).
        # f(x) = x//a + x//b - x//lcm
        # We need f(x) >= n and find minimal x.

        lo = 1
        hi = n * min(a, b)  # Upper bound: at worst, the nth multiple of the smaller number.
        # More precise upper bound: n * min(a, b) is safe since min(a,b)*n is at least the nth multiple.
        # But could be tighter: we could use n * a + n * b, but this is fine and simple.

        # Perform binary search on the answer.
        while lo < hi:
            mid = (lo + hi) // 2
            # Count magical numbers <= mid.
            count = mid // a + mid // b - mid // lcm
            if count < n:
                lo = mid + 1
            else:
                hi = mid

        return lo % MOD