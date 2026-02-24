from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        Compute the maximum XOR of two numbers in the array.
        Uses a bitwise prefix mask approach:
        - Build prefixes of numbers considering the top bits from current bit to MSB.
        - Check if there exist two prefixes that can achieve a candidate maximum when XORed.
        - If such pair exists, we can set the current bit in the result; otherwise it stays 0.
        Time: O(31 * n), Space: O(n) for the set of prefixes per iteration.
        """
        max_xor = 0
        mask = 0

        # Since nums[i] <= 2^31 - 1, the highest bit index is 30.
        for i in range(30, -1, -1):
            # Extend the mask to include the current bit and above.
            mask |= (1 << i)

            # Collect all unique prefixes of numbers with the current mask.
            prefixes = set(num & mask for num in nums)

            # Potential maximum with the current bit set to 1.
            candidate = max_xor | (1 << i)

            # If there exist two prefixes p1, p2 such that p1 ^ p2 == candidate,
            # then we can achieve this new maximum; update max_xor accordingly.
            found = False
            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    found = True
                    break

            if found:
                max_xor = candidate

        return max_xor