class Solution:
    def isValid(self, s: str) -> bool:
        # Odd length can never be fully paired.
        if len(s) % 2 == 1:
            return False

        # Map each closing bracket to the opening bracket it requires.
        matching_open = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []

        for ch in s:
            # Opening brackets are deferred until we see what closes them.
            if ch not in matching_open:
                stack.append(ch)
                continue

            # A closing bracket without a prior opener is immediately invalid.
            if not stack:
                return False

            # The most recent unmatched opener must match this closer.
            if stack[-1] != matching_open[ch]:
                return False

            stack.pop()

        # Valid only if every opener found a matching closer.
        return not stack