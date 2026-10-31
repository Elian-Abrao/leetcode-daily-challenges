from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        n = len(price)

        # Keep only strictly beneficial offers: those cheaper than buying the items individually.
        # An offer that is not cheaper can never be part of an optimal solution.
        beneficial = []
        for offer in special:
            # offer has n + 1 elements; last element is the bundle price
            individual_sum = 0
            for i in range(n):
                individual_sum += price[i] * offer[i]
            # Only keep offers that are strictly cheaper than individual purchase
            if offer[n] < individual_sum:
                beneficial.append(offer)

        @lru_cache(maxsize=None)
        def dfs(needs_tuple: tuple) -> int:
            """
            Returns the minimum cost to satisfy exactly the given needs.
            needs_tuple is a tuple of length n representing remaining quantities.
            """
            # Base case: nothing left to buy -> cost 0
            if all(v == 0 for v in needs_tuple):
                return 0

            # Baseline: buy everything without using any special offers
            best = sum(price[i] * needs_tuple[i] for i in range(n))

            # Try each beneficial special offer
            for offer in beneficial:
                # Check whether we can apply this offer (no item exceeds the need)
                possible = True
                new_needs = []
                for i in range(n):
                    if offer[i] > needs_tuple[i]:
                        possible = False
                        break
                    new_needs.append(needs_tuple[i] - offer[i])
                if not possible:
                    continue

                # Recursively compute cost after applying this offer
                cost = offer[n] + dfs(tuple(new_needs))
                if cost < best:
                    best = cost

            return best

        # Convert needs list to tuple for memoisation (hashable)
        return dfs(tuple(needs))