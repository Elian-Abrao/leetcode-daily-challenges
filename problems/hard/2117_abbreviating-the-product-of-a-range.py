import math

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        A = 1          # product with all 2s and 5s removed
        c2 = 0         # total count of factor 2 in the range
        c5 = 0         # total count of factor 5 in the range
        logP = 0.0     # sum of log10(i) for digits estimation

        # Iterate through the range to accumulate:
        # - number of 2s and 5s (for trailing zeros)
        # - the remaining product after stripping 2s and 5s
        for i in range(left, right + 1):
            logP += math.log10(i)
            x = i
            while x % 2 == 0:
                c2 += 1
                x //= 2
            while x % 5 == 0:
                c5 += 1
                x //= 5
            A *= x

        C = min(c2, c5)      # number of trailing zeros in P
        exp2 = c2 - C        # remaining powers of 2 after removing zeros
        exp5 = c5 - C        # remaining powers of 5 after removing zeros

        # Exact value of P without trailing zeros is N' = A * 2^exp2 * 5^exp5
        Nprime = A * (2 ** exp2) * (5 ** exp5)

        digits_total = int(math.floor(logP)) + 1
        d = digits_total - C      # digits after removing trailing zeros

        MOD = 100000  # last 5 digits extraction base

        if d > 10:
            # Need only the first 5 digits and last 5 digits after removing zeros
            X = logP - C
            f = X - math.floor(X)  # fractional part of log10(P) - C
            # Leading 5 digits: floor(10^(f + 4))
            leading5 = int(10 ** (f + 4) + 1e-9)
            # Last 5 digits: N' modulo 100000
            last5 = (A % MOD)
            last5 = (last5 * pow(2, exp2, MOD)) % MOD
            last5 = (last5 * pow(5, exp5, MOD)) % MOD
            return f"{leading5:05d}...{last5:05d}e{C}"
        else:
            # If digits <= 10, output the full N' exactly, followed by eC
            return f"{Nprime}e{C}"