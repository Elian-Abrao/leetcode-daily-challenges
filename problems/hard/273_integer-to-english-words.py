class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                    "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            if n < 20:
                return below_20[n]
            if n < 100:
                t = tens[n // 10]
                return t + ("" if n % 10 == 0 else " " + below_20[n % 10])
            return below_20[n // 100] + " Hundred" + ("" if n % 100 == 0 else " " + helper(n % 100))

        res = []
        i = 0
        while num > 0:
            rem = num % 1000
            if rem != 0:
                chunk = helper(rem)
                if thousands[i]:
                    chunk += " " + thousands[i]
                res.insert(0, chunk)
            num //= 1000
            i += 1

        return " ".join(res).strip()