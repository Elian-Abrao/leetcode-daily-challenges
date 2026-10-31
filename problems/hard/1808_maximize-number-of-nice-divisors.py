class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        n = primeFactors

        # Base case: with only one prime factor, the only nice divisor is n itself.
        if n == 1:
            return 1

        # Partition n into a sum of integers >= 2 to maximise their product.
        # The optimal strategy is to use as many 3's as possible.
        q, r = divmod(n, 3)

        if r == 0:
            # Exactly divisible by 3.
            return pow(3, q, MOD)
        if r == 1:
            # n = 3*(q-1) + 4  (since 4 = 2+2 yields product 4 > 3*1)
            return (pow(3, q - 1, MOD) * 4) % MOD
        # r == 2: n = 3*q + 2
        return (pow(3, q, MOD) * 2) % MOD