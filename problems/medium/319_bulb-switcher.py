import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb is toggled once for every divisor of its position.
        # Most numbers have divisors in pairs, so their bulbs end up off.
        # Only perfect squares have an odd number of divisors,
        # because one divisor pair collapses into the same number.
        #
        # Therefore, the answer is exactly the count of perfect squares <= n,
        # which is floor(sqrt(n)).
        return math.isqrt(n)