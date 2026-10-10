from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # The placement condition is equivalent to comparing sorted dimension triples.
        # Sorting each cuboid makes the height the largest dimension, which is always optimal
        # because it maximizes contribution without affecting whether it can be placed.
        for cuboid in cuboids:
            cuboid.sort()

        # In any valid stack, dimensions are non-decreasing from top to bottom.
        # Sorting lexicographically ensures that if cuboid A can be placed on cuboid B,
        # then A appears before B, so every valid stack is a subsequence of this order.
        cuboids.sort(key=lambda x: (x[0], x[1], x[2]))

        n = len(cuboids)
        # dp[i] = maximum total height of a stack whose bottom cuboid is i.
        dp = [cuboid[2] for cuboid in cuboids]

        for i in range(n):
            ci = cuboids[i]
            for j in range(i):
                cj = cuboids[j]
                # cuboid j can be placed on top of cuboid i.
                if cj[0] <= ci[0] and cj[1] <= ci[1] and cj[2] <= ci[2]:
                    dp[i] = max(dp[i], dp[j] + ci[2])

        return max(dp)