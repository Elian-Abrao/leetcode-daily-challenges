class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        # Compute total candies for both
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)

        # After one-for-one exchange, each should have (sum_a + sum_b) / 2.
        # Let diff = target - sum_a = (sum_b - sum_a) / 2.
        # So we need a from Alice and b = a + diff from Bob.
        # diff is integer because total is even (guaranteed by existence of answer).
        diff = (sum_b - sum_a) // 2

        # Use a set for O(1) lookups of Bob's sizes.
        bob_set = set(bobSizes)

        # Find the first pair (a, a+diff) where a in Alice and a+diff in Bob.
        for a in aliceSizes:
            b = a + diff
            if b in bob_set:
                return [a, b]

        # According to the problem statement, a valid answer always exists.
        # This line is unreachable but added for completeness.
        return []