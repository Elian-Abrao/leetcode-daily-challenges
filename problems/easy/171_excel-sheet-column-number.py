class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Interpret the title as a base-26 number where A..Z map to 1..26.
        # This differs from normal base conversion because there is no zero digit.
        column_number = 0

        for char in columnTitle:
            # Shift previous digits left in base 26, then add current letter value.
            # Example: "AB" -> ((0 * 26 + 1) * 26 + 2) = 28.
            column_number = column_number * 26 + (ord(char) - ord('A') + 1)

        return column_number