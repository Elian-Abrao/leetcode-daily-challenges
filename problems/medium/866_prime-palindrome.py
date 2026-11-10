class Solution:
    def primePalindrome(self, n: int) -> int:
        import math

        # ---------- handle small n (answer belongs to {2,3,5,7,11}) ----------
        if n <= 11:
            for p in (2, 3, 5, 7, 11):
                if p >= n:
                    return p

        # ---------- constants ----------
        MAX_VAL = 2 * 10**8          # guaranteed upper bound for the answer

        # ---------- sieve: primes up to sqrt(MAX_VAL) ≈ 14142 ----------
        sqrt_max = math.isqrt(MAX_VAL)
        limit = sqrt_max + 1         # inclusive size of the sieve

        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, math.isqrt(limit) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
        primes = [i for i, ok in enumerate(sieve) if ok]

        # ---------- primality test for numbers ≤ MAX_VAL ----------
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            # trial division by pre‑computed primes
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    return False
            return True

        # ---------- integer reversal (avoid string conversion) ----------
        def reverse_int(x: int) -> int:
            rev = 0
            while x:
                rev = rev * 10 + (x % 10)
                x //= 10
            return rev

        # ---------- generate odd‑length palindromes ----------
        # Every even‑length palindrome > 11 is divisible by 11,
        # therefore for n > 11 we only examine odd lengths.
        L = 3                        # start with length 3 (e.g. 101)
        while L <= 9:                # 9 digits cover up to 200 000 000
            k = L // 2               # L = 2k + 1
            pow10_k = 10 ** k
            # the first half (including middle) has k+1 digits
            start_root = pow10_k
            end_root = 10 ** (k + 1) - 1

            for root in range(start_root, end_root + 1):
                # Build palindrome = root * 10^k + reverse(root // 10)
                rev_part = reverse_int(root // 10)
                pal = root * pow10_k + rev_part

                # No need to look beyond the guaranteed bound
                if pal > MAX_VAL:
                    break
                if pal < n:
                    continue
                if is_prime(pal):
                    return pal

            L += 2                   # next odd length

        # According to the problem statement we never reach this line.
        return -1