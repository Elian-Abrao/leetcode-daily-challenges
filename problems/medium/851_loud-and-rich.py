from __future__ import annotations
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        For each person x, find the y (including x) with the minimum quiet value
        among all people that are known to have at least as much money as x.
        The 'richer' array provides direct richer->poorer relationships,
        which form a DAG. We compute answers by DFS with memoization.
        """
        n = len(quiet)
        # reverse adjacency: for each person, list of those who are directly richer
        rev_adj = [[] for _ in range(n)]
        for a, b in richer:
            # a is richer than b => a is a candidate for the answer of b
            rev_adj[b].append(a)

        # memo[x] = person id with least quiet among all that have >= money than x
        memo = [None] * n

        def dfs(x: int) -> int:
            """Return the answer for person x (the best candidate)."""
            if memo[x] is not None:
                return memo[x]

            # start with the person itself
            best = x
            # check all direct richer people
            for p in rev_adj[x]:
                candidate = dfs(p)
                if quiet[candidate] < quiet[best]:
                    best = candidate
            memo[x] = best
            return best

        # Compute answer for every person
        return [dfs(i) for i in range(n)]