from __future__ import annotations

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Helper to extract real and imaginary parts from "a+bi" string
        def parse(s: str) -> tuple[int, int]:
            # Split on '+' to separate real part and the imaginary part (includes trailing 'i')
            real_part, imag_part = s.split('+')
            # Remove the final 'i' from the imaginary part and convert to int
            imag = int(imag_part.rstrip('i'))
            return int(real_part), imag

        # Parse both inputs
        a, b = parse(num1)
        c, d = parse(num2)

        # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real = a * c - b * d
        imag = a * d + b * c

        # Format result as required "real+imaginaryi"
        return f"{real}+{imag}i"