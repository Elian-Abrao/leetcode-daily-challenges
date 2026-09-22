from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        Returns the string representation of the expression that yields the
        maximum value when evaluating the division chain with parentheses.

        Key insight: To maximise a1 / a2 / ... / an, we want the denominator as
        small as possible.  The best we can do is to turn all numbers from a3
        onward into multipliers of a1, which is achieved by:
            a1 / (a2 / a3 / ... / an)
        This way the denominator reduces to a2 divided by the product of a3..an,
        giving a result of (a1 * a3 * ... * an) / a2.
        """
        n = len(nums)

        # Trivial cases that need no parentheses
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"

        # For n >= 3: optimal expression is a1/(a2/a3/.../an)
        # The inner chain (a2/a3/.../an) is already left‑associative,
        # so no extra parentheses are needed inside.
        return f"{nums[0]}/(" + "/".join(map(str, nums[1:])) + ")"