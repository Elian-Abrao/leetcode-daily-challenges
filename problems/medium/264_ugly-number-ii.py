class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # The sequence is defined to start with 1.
        # This also serves as the seed for generating all later ugly numbers.
        ugly_numbers = [1] * n

        # Each pointer marks the smallest ugly number that has not yet been used
        # to generate a candidate multiple for 2, 3, or 5.
        index2 = 0
        index3 = 0
        index5 = 0

        for i in range(1, n):
            # The next ugly number must be the smallest unseen product.
            next_by_2 = ugly_numbers[index2] * 2
            next_by_3 = ugly_numbers[index3] * 3
            next_by_5 = ugly_numbers[index5] * 5

            next_ugly = min(next_by_2, next_by_3, next_by_5)
            ugly_numbers[i] = next_ugly

            # Advance every pointer that produced the chosen value.
            # This is crucial for deduplication: 6 can come from both 2*3 and 3*2.
            if next_ugly == next_by_2:
                index2 += 1
            if next_ugly == next_by_3:
                index3 += 1
            if next_ugly == next_by_5:
                index5 += 1

        # n is at least 1, so the last filled entry is the answer.
        return ugly_numbers[-1]