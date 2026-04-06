class Solution:
    def myAtoi(self, s: str) -> int:
        # 32-bit signed integer bounds required by the problem.
        int_min = -(1 << 31)
        int_max = (1 << 31) - 1

        n = len(s)
        i = 0

        # Skip only leading spaces; other whitespace characters do not exist here.
        while i < n and s[i] == " ":
            i += 1

        # Empty string or string with only spaces cannot produce a number.
        if i == n:
            return 0

        # Read an optional sign once, before any digits.
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        value = 0
        has_digits = False

        # Build the number digit by digit until the first non-digit.
        while i < n and "0" <= s[i] <= "9":
            has_digits = True
            digit = ord(s[i]) - ord("0")

            # Clamp early to avoid growing beyond useful precision.
            # The cutoff differs by sign because -2^31 has one extra unit of magnitude.
            limit = int_max if sign == 1 else -int_min
            if value > (limit - digit) // 10:
                return int_max if sign == 1 else int_min

            value = value * 10 + digit
            i += 1

        # No digits after optional spaces/sign means the result is zero.
        if not has_digits:
            return 0

        return sign * value