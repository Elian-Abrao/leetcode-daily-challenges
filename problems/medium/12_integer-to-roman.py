class Solution:
    def intToRoman(self, num: int) -> str:
        # Define values and corresponding roman symbols in descending order.
        # Include subtractive forms (CM, CD, XC, XL, IX, IV) as single entries.
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        res = []  # Collect pieces of the final roman numeral
        # Greedy approach: for each value from largest to smallest, append symbol
        # as many times as it fits into the remaining number.
        for v, s in zip(values, symbols):
            if num == 0:
                break  # Early exit if nothing left to convert
            count, num = divmod(num, v)  # count how many times v fits into num
            if count > 0:
                res.append(s * count)  # append the symbol repeated 'count' times
        
        return "".join(res)