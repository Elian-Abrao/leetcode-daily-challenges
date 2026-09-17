class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        """
        Constructs an array of length n containing numbers 1..n such that
        the absolute differences between consecutive elements contain exactly
        k distinct integers.

        Approach:
        - The first (n - k - 1) elements are placed in increasing order (1, 2, ...).
          This contributes only difference 1 repeatedly.
        - The remaining (k + 1) elements are placed in a "zigzag" pattern
          starting from the two ends of the remaining range, which generates
          k distinct differences (k, k-1, ..., 1).
        """
        # Build the first part: consecutive numbers from 1 to n-k-1.
        # These produce differences of 1 only.
        result = list(range(1, n - k))

        # Remaining numbers: left = n - k, right = n.
        left = n - k
        right = n

        # Alternate between picking from left end and right end.
        toggle = True
        while left <= right:
            if toggle:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
            toggle = not toggle

        return result