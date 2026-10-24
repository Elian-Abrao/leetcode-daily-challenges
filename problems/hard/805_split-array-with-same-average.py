class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        total = sum(nums)
        # If all numbers are zero, any non‑empty proper subset works for n >= 2.
        if total == 0:
            return True

        # Only need to check subset sizes <= n//2 because a valid larger subset
        # implies a valid complement of size <= n//2.
        max_k = n // 2

        # Mask to keep only sums in [0, total] after shifting.
        mask = (1 << (total + 1)) - 1

        # dp[c] is a bitset: bit s is 1 iff sum s can be achieved with exactly c elements.
        dp = [0] * (max_k + 1)
        dp[0] = 1  # sum 0 with 0 elements

        for x in nums:
            # Update in reverse count order to use each element at most once.
            # Only counts up to max_k-1 need to be extended.
            for c in range(max_k - 1, -1, -1):
                if dp[c]:
                    new_sums = (dp[c] << x) & mask
                    dp[c + 1] |= new_sums

        # Check for each possible size k (1..max_k) whether there is a subset
        # with sum = (total * k) / n (must be integer).
        for k in range(1, max_k + 1):
            if (total * k) % n != 0:
                continue
            target = (total * k) // n
            if (dp[k] >> target) & 1:
                return True

        return False