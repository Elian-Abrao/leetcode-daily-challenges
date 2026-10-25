class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Primes up to 20 (since numbers <= 10^6 need at most 20 bits)
        PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for num in range(left, right + 1):
            # int.bit_count() is efficient and available in Python 3.8+
            # For older environments, use bin(num).count('1')
            if num.bit_count() in PRIMES:
                count += 1
        return count