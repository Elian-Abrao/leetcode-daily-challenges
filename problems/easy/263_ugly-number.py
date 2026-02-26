class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers are positive and only have prime factors among {2, 3, 5}
        if n <= 0:
            return False

        # Repeatedly divide by 2, 3, and 5 to remove their factors
        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor

        # If fully reduced, remaining should be 1
        return n == 1