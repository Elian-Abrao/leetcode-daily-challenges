class Solution:
    def solveEquation(self, equation: str) -> str:
        # Parse one side of the equation, return (coeff_of_x, constant_sum)
        def parse_side(s: str):
            coeff = 0
            const = 0
            n = len(s)
            i = 0
            sign = 1  # current sign for the next term
            while i < n:
                # Read optional sign
                if s[i] == '+':
                    sign = 1
                    i += 1
                elif s[i] == '-':
                    sign = -1
                    i += 1
                else:
                    # No explicit sign means positive (handled after number)
                    pass

                # Read number if present (could be multi-digit)
                num = None
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                if start < i:
                    num = int(s[start:i])

                # Determine if this is an 'x' term or a constant
                if i < n and s[i] == 'x':
                    # Coefficient term: if no number was parsed, coefficient is 1
                    coeff += sign * (num if num is not None else 1)
                    i += 1
                else:
                    # Constant term: number must exist
                    const += sign * num
            return coeff, const

        # Split equation into left and right sides
        left_str, right_str = equation.split('=', 1)

        left_coeff, left_const = parse_side(left_str)
        right_coeff, right_const = parse_side(right_str)

        # Bring all terms to left side: (left_coeff - right_coeff)*x + (left_const - right_const) = 0
        total_coeff = left_coeff - right_coeff
        total_const = left_const - right_const

        # Solve: total_coeff * x = -total_const  (move constant to right)
        # => x = -total_const / total_coeff
        # But careful: we moved constant to right: left - right = 0
        # Actually total_coeff * x + total_const = 0  => total_coeff * x = -total_const
        required_const = -total_const

        if total_coeff == 0:
            if required_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            # Guaranteed integer division by problem statement
            x = required_const // total_coeff
            return f"x={x}"