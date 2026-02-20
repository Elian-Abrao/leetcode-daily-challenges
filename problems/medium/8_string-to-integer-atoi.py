class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # Determine sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # Read digits
        result = 0
        started = False
        while i < n and s[i].isdigit():
            started = True
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1

        if not started:
            return 0

        result *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result