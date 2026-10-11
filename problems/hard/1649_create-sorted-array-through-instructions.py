from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7

        # Fenwick tree counts how many times each value has been inserted.
        max_val = max(instructions)
        bit = [0] * (max_val + 2)  # 1-indexed Fenwick tree

        def update(idx: int, delta: int) -> None:
            """Add delta to value at idx (1-based)."""
            while idx <= max_val:
                bit[idx] += delta
                idx += idx & -idx

        def query(idx: int) -> int:
            """Return prefix sum of frequencies for values 1..idx."""
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        total_cost = 0
        inserted = 0

        for x in instructions:
            # Number of already inserted elements strictly less than x
            less = query(x - 1)

            # query(x) counts elements <= x, so greater = inserted - query(x)
            greater = inserted - query(x)

            total_cost = (total_cost + min(less, greater)) % MOD

            # Insert current value into the Fenwick tree
            update(x, 1)
            inserted += 1

        return total_cost