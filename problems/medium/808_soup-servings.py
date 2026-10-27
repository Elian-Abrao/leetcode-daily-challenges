from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        # Convert the original volume to the number of 25ml "servings".
        # Using ceiling division ensures we do not underestimate.
        servings = (n + 24) // 25

        # For a large number of servings, the probability that A runs out
        # before B is extremely close to 1 (within 1e-5).  Empirical tests
        # show that servings > 200 guarantees this.
        if servings > 200:
            return 1.0

        @lru_cache(maxsize=None)
        def dfs(a: int, b: int) -> float:
            """
            Returns the probability that soup A is emptied before soup B,
            plus half the probability that both are emptied in the same turn,
            starting from a servings of A and b servings of B.
            """
            # If both are (or become) empty at the same time, the turn
            # contributes half a win.
            if a <= 0 and b <= 0:
                return 0.5
            # A is empty, B is not -> A empties first (full win).
            if a <= 0:
                return 1.0
            # B is empty, A is not -> B empties first (no win).
            if b <= 0:
                return 0.0

            # Four operations, each with probability 0.25.
            # If an operation would pour more than the remaining amount,
            # only the available amount is poured (which effectively makes
            # the corresponding state become (0, ...) or (..., 0)).
            # The recursive call automatically handles negative indices
            # by checking the base cases above.
            prob = 0.25 * (
                dfs(a - 4, b) +       # (100, 0)
                dfs(a - 3, b - 1) +   # (75,  25)
                dfs(a - 2, b - 2) +   # (50,  50)
                dfs(a - 1, b - 3)     # (25,  75)
            )
            return prob

        return dfs(servings, servings)