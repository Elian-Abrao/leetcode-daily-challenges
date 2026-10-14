from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        # Binary search for the first character strictly greater than target.
        # bisect_right returns the insertion point after any existing occurrences
        # of target, which is exactly the index of the smallest character > target.
        pos = bisect_right(letters, target)

        # If pos equals the length, wrap around to the first character.
        if pos == len(letters):
            return letters[0]
        # Otherwise, the found character is the answer.
        return letters[pos]