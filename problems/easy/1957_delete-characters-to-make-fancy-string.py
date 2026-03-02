class Solution:
    def makeFancyString(self, s: str) -> str:
        # Build the resulting string with at most two identical consecutive characters.
        # If the last two characters in the result are the same as the current character,
        # skipping this character preserves the "no three consecutive equal" invariant.
        res = []
        for ch in s:
            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                # Skipping this character would create a triple of the same letter.
                continue
            res.append(ch)
        return ''.join(res)