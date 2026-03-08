from typing import List
from collections import Counter


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression keeps future lookups almost constant time.
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        # Union by size avoids tall trees in adversarial merge orders.
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        max_value = max(nums)

        # Smallest prime factor sieve lets us factor every number quickly.
        spf = list(range(max_value + 1))
        for i in range(2, int(max_value ** 0.5) + 1):
            if spf[i] == i:
                start = i * i
                for multiple in range(start, max_value + 1, i):
                    if spf[multiple] == multiple:
                        spf[multiple] = i

        def prime_factors(value: int) -> List[int]:
            factors = []
            # We only need distinct primes, because repeated powers do not
            # create additional connectivity beyond the prime itself.
            while value > 1:
                prime = spf[value]
                factors.append(prime)
                while value % prime == 0:
                    value //= prime
            return factors

        uf = UnionFind(n)
        first_index_by_factor = {}

        for index, value in enumerate(nums):
            for factor in prime_factors(value):
                if factor in first_index_by_factor:
                    # Any shared prime factor means both numbers belong
                    # to the same connected component.
                    uf.union(index, first_index_by_factor[factor])
                else:
                    first_index_by_factor[factor] = index

        # Count nodes by final representative to get component sizes.
        component_sizes = Counter(uf.find(i) for i in range(n))
        return max(component_sizes.values())