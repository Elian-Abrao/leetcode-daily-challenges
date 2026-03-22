from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [0] * n
        current = 1

        for index in range(n):
            # The current number is always the next lexicographical value.
            result[index] = current

            if current * 10 <= n:
                # Go to the smallest child first, which is the next lexicographical number.
                current *= 10
            else:
                # If we cannot go deeper, move to the next valid sibling.
                # When no sibling exists, climb up until one does.
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1

        return result