from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = 10**18

        # dp[k][c] = minimum cost after processing current prefix,
        # forming exactly k neighborhoods, and ending with color c.
        dp = [[INF] * n for _ in range(target + 1)]

        # Initialize the first house directly so later transitions stay uniform.
        if houses[0] != 0:
            dp[1][houses[0] - 1] = 0
        else:
            for color in range(n):
                dp[1][color] = cost[0][color]

        # Process houses from left to right; each step only depends on the previous row.
        for index in range(1, m):
            new_dp = [[INF] * n for _ in range(target + 1)]

            # For each neighborhood count, precompute the best and second-best
            # ending colors. This lets us get "best previous color different from c"
            # in O(1) instead of scanning all colors every time.
            best = [(INF, -1, INF) for _ in range(target + 1)]
            for groups in range(1, target + 1):
                first_cost = INF
                first_color = -1
                second_cost = INF

                for color in range(n):
                    value = dp[groups][color]
                    if value < first_cost:
                        second_cost = first_cost
                        first_cost = value
                        first_color = color
                    elif value < second_cost:
                        second_cost = value

                best[groups] = (first_cost, first_color, second_cost)

            allowed_colors = [houses[index] - 1] if houses[index] != 0 else range(n)

            # We can never have more neighborhoods than houses considered so far.
            max_groups = min(target, index + 1)

            for groups in range(1, max_groups + 1):
                same_group_best, _, _ = best[groups]
                prev_group_best, prev_group_color, prev_group_second = best[groups - 1] if groups > 1 else (INF, -1, INF)

                for color in allowed_colors:
                    paint_cost = 0 if houses[index] != 0 else cost[index][color]

                    # Keep the same color as previous house: neighborhood count unchanged.
                    keep_same = dp[groups][color]

                    # Switch from a different previous color: neighborhood count increases by 1.
                    if groups > 1:
                        # If the globally best previous ending color equals current color,
                        # we must use the second-best to ensure the color actually changes.
                        switch_cost = prev_group_second if prev_group_color == color else prev_group_best
                    else:
                        switch_cost = INF

                    previous = keep_same if keep_same < switch_cost else switch_cost
                    if previous < INF:
                        new_dp[groups][color] = previous + paint_cost

            dp = new_dp

        answer = min(dp[target])
        return -1 if answer >= INF else answer