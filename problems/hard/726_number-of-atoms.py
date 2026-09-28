from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [defaultdict(int)]
        i = 0

        while i < n:
            ch = formula[i]

            if ch == '(':
                stack.append(defaultdict(int))
                i += 1

            elif ch == ')':
                top = stack.pop()
                i += 1
                # parse multiplier
                multiplier = 0
                digit_start = i
                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
                if i == digit_start:
                    multiplier = 1

                # Apply multiplier to the popped scope
                for atom, cnt in top.items():
                    top[atom] = cnt * multiplier

                # Merge into the parent scope
                current = stack[-1]
                for atom, cnt in top.items():
                    current[atom] += cnt

            else:
                # parse the element name
                atom_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[atom_start:i]

                # parse count (if any)
                count = 0
                digit_start = i
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if i == digit_start:
                    count = 1

                stack[-1][atom] += count

        final_counts = stack[0]
        result_parts = []
        for atom in sorted(final_counts):
            cnt = final_counts[atom]
            if cnt == 1:
                result_parts.append(atom)
            else:
                result_parts.append(f"{atom}{cnt}")
        return "".join(result_parts)