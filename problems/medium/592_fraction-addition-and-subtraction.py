from __future__ import annotations
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        res_num = 0
        res_den = 1

        n = len(expression)
        i = 0

        while i < n:
            sign = 1
            if expression[i] == '+':
                sign = 1
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            num_start = i
            while i < n and expression[i] != '/':
                i += 1
            numerator = int(expression[num_start:i])
            i += 1

            den_start = i
            while i < n and expression[i] not in ('+', '-'):
                i += 1
            denominator = int(expression[den_start:i])

            res_num = res_num * denominator + sign * numerator * res_den
            res_den = res_den * denominator

            g = gcd(abs(res_num), res_den)
            if g > 0:
                res_num //= g
                res_den //= g

        if res_num == 0:
            return "0/1"
        return f"{res_num}/{res_den}"