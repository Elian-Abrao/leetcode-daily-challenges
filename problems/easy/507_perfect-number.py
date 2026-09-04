import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # A perfect number must be positive and greater than 1.
        # 1 has no proper divisors (excluding itself), so it's not perfect.
        if num <= 1:
            return False

        # Start sum with divisor 1 (always a divisor for num > 1).
        divisor_sum = 1

        # Check divisors up to sqrt(num). Use integer sqrt for precision.
        limit = int(math.isqrt(num))
        for i in range(2, limit + 1):
            if num % i == 0:
                # i is a divisor; add it.
                divisor_sum += i
                # The paired divisor (num // i) is also a divisor, unless it's i itself.
                paired = num // i
                if paired != i:
                    divisor_sum += paired

        # If the sum of all proper divisors equals the number, it's perfect.
        return divisor_sum == num