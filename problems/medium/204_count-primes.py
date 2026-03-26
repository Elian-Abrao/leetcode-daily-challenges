class Solution:
    def countPrimes(self, n: int) -> int:
        # No primes exist below 2.
        if n <= 2:
            return 0

        # Sieve[i] tells whether i is still considered prime.
        # bytearray is memory-efficient for constraints up to 5 * 10^6.
        is_prime = bytearray(b"\x01") * n
        is_prime[0] = 0
        is_prime[1] = 0

        # Only need to cross out multiples starting from p * p:
        # any smaller multiple already has a smaller prime factor.
        limit = int(n ** 0.5) + 1
        for candidate in range(2, limit):
            if is_prime[candidate]:
                start = candidate * candidate
                step = candidate

                # Mark all multiples of the current prime as composite.
                # Slice assignment keeps the implementation compact and fast.
                is_prime[start:n:step] = b"\x00" * (((n - 1 - start) // step) + 1)

        # Remaining true entries are exactly the primes below n.
        return sum(is_prime)