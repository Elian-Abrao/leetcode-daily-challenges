class Solution:
    def convertToBase7(self, num: int) -> str:
        # Special case: zero always maps to "0"
        if num == 0:
            return "0"

        # Remember sign; work with absolute value for division
        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        # Extract least-significant digits repeatedly
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        # Digits were collected in reverse order (LSB first)
        return sign + "".join(reversed(digits))