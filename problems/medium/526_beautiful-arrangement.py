class Solution:
    def countArrangement(self, n: int) -> int:
        """
        Returns the number of beautiful arrangements for integers 1..n.
        A permutation perm[1..n] is beautiful if for every i:
            perm[i] % i == 0  or  i % perm[i] == 0.
        Uses bitmask DP over subsets: dp[mask] = number of ways to arrange
        the numbers indicated by the set bits (1-indexed) into positions 1..k
        where k = popcount(mask). The next position to fill is k+1.
        """
        # Total number of masks for n elements
        total_masks = 1 << n
        dp = [0] * total_masks
        dp[0] = 1  # empty arrangement

        # Process masks in increasing order (more bits = later positions)
        for mask in range(total_masks):
            # Number of placed numbers = popcount(mask)
            placed = mask.bit_count()  # Python 3.8+; fallback: bin(mask).count('1')
            pos = placed + 1  # current position to fill (1-indexed)

            # Try every unused number j (1..n)
            for j in range(1, n + 1):
                bit = 1 << (j - 1)
                if mask & bit:  # already used
                    continue
                # Condition for beautiful arrangement at this position
                if j % pos == 0 or pos % j == 0:
                    dp[mask | bit] += dp[mask]

        # Full mask has all numbers placed
        return dp[total_masks - 1]