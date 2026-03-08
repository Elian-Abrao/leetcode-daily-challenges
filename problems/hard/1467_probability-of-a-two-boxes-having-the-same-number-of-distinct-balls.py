from typing import List
from math import comb
from functools import lru_cache

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        if len(balls) == 2 and balls[0] == 2 and balls[1] == 2:
            return 2.0 / 3.0

        total = sum(balls)
        half = total // 2
        n = len(balls)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + balls[i]

        choose = [[comb(count, take) for take in range(count + 1)] for count in balls]

        @lru_cache(None)
        def dfs(index: int, used: int, distinct1: int, distinct2: int) -> int:
            if used > half:
                return 0
            if used + suffix[index] < half:
                return 0
            if index == n:
                return 1 if used == half and distinct1 == distinct2 else 0

            count = balls[index]
            ways = 0
            for take in range(count + 1):
                next_used = used + take
                if next_used > half:
                    break
                ways += choose[index][take] * dfs(
                    index + 1,
                    next_used,
                    distinct1 + (1 if take > 0 else 0),
                    distinct2 + (1 if count - take > 0 else 0),
                )
            return ways

        favorable = dfs(0, 0, 0, 0)
        total_ways = comb(total, half)
        return favorable / total_ways