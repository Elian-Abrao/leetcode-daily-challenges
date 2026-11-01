class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        """
        Returns the intervals (start, end) of every group of 3 or more
        consecutive identical characters, sorted by start index.
        Time: O(n), Space: O(1) auxiliary (output excluded).
        """
        n = len(s)
        result = []
        i = 0  # scanning index

        while i < n:
            # Start of a new group
            start = i
            current_char = s[i]

            # Extend the group while the same character repeats
            while i < n and s[i] == current_char:
                i += 1

            # end is the last index of the group (inclusive)
            end = i - 1

            # A group is "large" if it has at least 3 characters
            if end - start + 1 >= 3:
                result.append([start, end])

        return result