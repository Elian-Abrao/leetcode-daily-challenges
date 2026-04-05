class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Excel columns are 1-indexed, unlike normal base-26 digits.
        # Subtract 1 before each step so that:
        # 1 -> 0 -> 'A', 26 -> 25 -> 'Z', 27 -> 0 then 0 -> 'AA'.
        characters = []

        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            characters.append(chr(ord('A') + remainder))

        # Digits are produced from least significant to most significant.
        characters.reverse()
        return ''.join(characters)