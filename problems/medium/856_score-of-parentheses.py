class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # The score can be computed by tracking the current depth.
        # Every "()" contributes 2^depth, where depth is the nesting level of the pair.
        depth = 0
        score = 0
        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                # If this ')' closes a pair directly, i.e., it is preceded by '(', it's an atomic "()" at this depth.
                if i > 0 and s[i - 1] == '(':
                    score += 1 << depth
        return score