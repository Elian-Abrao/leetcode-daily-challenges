class Solution:
    def minSteps(self, n: int) -> int:
        # For n == 1, no operations are needed.
        if n <= 1:
            return 0

        # The minimal number of operations equals the sum of prime factors
        # of n (with multiplicity). This follows from building up n by
        # repeatedly performing Copy All once per prime factor and Paste
        # (factor value) - effectively decomposing n into its prime factors.
        total_steps = 0
        divisor = 2

        # Factorize n by trial division up to sqrt(n).
        while divisor * divisor <= n:
            while n % divisor == 0:
                total_steps += divisor
                n //= divisor
            divisor += 1

        # If n > 1 here, it is a prime factor larger than sqrt(original_n).
        if n > 1:
            total_steps += n

        return total_steps