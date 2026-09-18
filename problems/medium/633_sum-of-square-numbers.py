from __future__ import annotations
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Determines whether there exist two integers a and b such that
        a^2 + b^2 = c, using a two-pointer approach on the sorted squares.
        Time: O(sqrt(c)), Space: O(1).
        """
        # Start with the smallest possible square (0^2) and the largest
        # possible square (floor(sqrt(c))^2, since a,b cannot exceed sqrt(c)).
        a = 0
        b = int(math.isqrt(c))  # integer square root of c

        while a <= b:
            current_sum = a * a + b * b

            if current_sum == c:
                return True
            elif current_sum < c:
                # Increase the smaller term to grow the sum
                a += 1
            else:  # current_sum > c
                # Decrease the larger term to shrink the sum
                b -= 1

        # No pair found
        return False