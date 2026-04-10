class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        # Each value stack entry is (cost_to_make_0, cost_to_make_1).
        # This is stronger than storing only the current value: it lets us
        # recompute the best way to flip any subexpression after future merges.
        values = []
        ops = []

        def combine(left, right, op):
            l0, l1 = left
            r0, r1 = right

            # Costs if we keep the operator as '&'.
            # AND becomes 1 only when both sides are 1.
            and0 = min(l0 + r0, l0 + r1, l1 + r0)
            and1 = l1 + r1

            # Costs if we keep the operator as '|'.
            # OR becomes 0 only when both sides are 0.
            or0 = l0 + r0
            or1 = min(l1 + r0, l0 + r1, l1 + r1)

            # We may also spend 1 operation to flip the operator itself.
            if op == '&':
                return min(and0, 1 + or0), min(and1, 1 + or1)
            return min(or0, 1 + and0), min(or1, 1 + and1)

        def apply_top():
            # Apply the most recent pending binary operation.
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            values.append(combine(left, right, op))

        for ch in expression:
            if ch == '0':
                # A literal already evaluates to 0, and needs one flip to become 1.
                values.append((0, 1))
            elif ch == '1':
                # Symmetric case for literal 1.
                values.append((1, 0))
            elif ch == '(':
                # Parentheses block reductions until the matching ')'.
                ops.append(ch)
            elif ch == ')':
                # Fully reduce the parenthesized subexpression.
                while ops and ops[-1] != '(':
                    apply_top()
                ops.pop()  # Remove '('.
            else:
                # '&' and '|' have the same precedence here, and evaluation is
                # strictly left-to-right, so reduce any pending operator first.
                while ops and ops[-1] != '(':
                    apply_top()
                ops.append(ch)

        # Reduce the remaining top-level chain.
        while ops:
            apply_top()

        cost0, cost1 = values[-1]

        # Exactly one target cost is 0 for the current final value.
        # The other cost is the minimum cost to flip that final value.
        return cost1 if cost0 == 0 else cost0