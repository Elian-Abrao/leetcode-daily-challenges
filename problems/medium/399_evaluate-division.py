from __future__ import annotations
from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build a bidirectional graph where edge A->B has weight value A/B
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        results: List[float] = []
        for c, d in queries:
            # If either variable is unseen, the division cannot be determined
            if c not in graph or d not in graph:
                results.append(-1.0)
                continue
            # If asking for the same variable, the quotient is 1
            if c == d:
                results.append(1.0)
                continue

            # DFS with accumulation: current product represents the value from start to current node
            visited = set()
            stack = [(c, 1.0)]
            found = False

            while stack:
                node, acc = stack.pop()
                if node == d:
                    results.append(acc)
                    found = True
                    break
                if node in visited:
                    continue
                visited.add(node)

                for nei, w in graph[node].items():
                    if nei not in visited:
                        stack.append((nei, acc * w))

            if not found:
                results.append(-1.0)

        return results