from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        """
        Simulates writing the string 's' across lines of at most 100 pixels.
        Returns [number_of_lines, width_of_last_line].
        """
        if not s:                     # edge case (not required by constraints, but safe)
            return [0, 0]

        # ord('a') base for quick index calculation
        base = ord('a')
        # Start with one line, no width used yet.
        lines = 1
        current_width = 0

        for ch in s:
            # width of the current character according to the given array
            w = widths[ord(ch) - base]

            # Check whether adding this character would overflow the current line.
            if current_width + w > 100:
                # Move to the next line; start with this character's width.
                lines += 1
                current_width = w
            else:
                # Stay on the same line.
                current_width += w

        return [lines, current_width]