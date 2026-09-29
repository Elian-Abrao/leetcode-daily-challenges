class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        m = len(digits)

        i = 0
        while i + 1 < m and digits[i] <= digits[i + 1]:
            i += 1

        if i == m - 1:
            return n

        while i > 0 and digits[i - 1] == digits[i]:
            i -= 1

        digits[i] = str(int(digits[i]) - 1)

        for j in range(i + 1, m):
            digits[j] = '9'

        return int(''.join(digits))