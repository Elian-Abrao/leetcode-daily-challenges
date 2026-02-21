from __future__ import annotations

class Solution:
    def findNthDigit(self, n: int) -> int:
        # Determine which group of numbers the nth digit falls into
        digits = 1       # current digit-length (1-digit numbers: 1..9)
        count = 9        # count of numbers with 'digits' digits

        # Subtract entire groups until n is within the current group
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10

        # Now n lies within the block of numbers that have 'digits' digits
        start = 10 ** (digits - 1)                 # first number with 'digits' digits
        index = (n - 1) // digits                   # which number in this block
        number = start + index                       # actual number containing the nth digit
        digit_index = (n - 1) % digits               # which digit inside 'number'
        return int(str(number)[digit_index])