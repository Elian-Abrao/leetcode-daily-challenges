class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end to avoid splitting the whole string.
        index = len(s) - 1

        # Ignore trailing spaces, since they are not part of the last word.
        while index >= 0 and s[index] == " ":
            index -= 1

        # Count consecutive non-space characters of the last word.
        length = 0
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1

        return length