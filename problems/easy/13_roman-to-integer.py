class Solution:
    def romanToInt(self, s: str) -> int:
        # Direct value lookup keeps the scan O(n) with constant extra space.
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0

        # Scan left to right. If a symbol is smaller than the next one,
        # it must be part of one of the valid subtractive pairs.
        for i, ch in enumerate(s):
            value = values[ch]

            # Subtract only when the next symbol is strictly larger.
            # Otherwise, this symbol contributes normally.
            if i + 1 < len(s) and value < values[s[i + 1]]:
                total -= value
            else:
                total += value

        return total