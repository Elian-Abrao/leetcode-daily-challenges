from __future__ import annotations

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Flip the image horizontally, then invert it (0->1, 1->0).
        Operates in-place for efficiency.
        """
        n = len(image)          # number of rows (also columns, square matrix)
        for row in image:
            # Use two pointers to flip and invert simultaneously
            left, right = 0, n - 1
            while left < right:
                # Swap and invert symmetric elements
                # XOR with 1 flips the bit: 0^1=1, 1^1=0
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1
            # If the row has an odd length, invert the middle element
            if left == right:   # middle index
                row[left] ^= 1
        return image