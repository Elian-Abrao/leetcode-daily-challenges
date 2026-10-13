class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        if len(result) != n:
            return False

        i = j = 0

        # Scan through both strings, skipping 'X's, and compare the non-X characters
        # in order. The relative order of 'L' and 'R' must be preserved.
        while i < n or j < n:
            # Skip 'X' characters in start: they are empty space for movement.
            while i < n and start[i] == 'X':
                i += 1
            # Skip 'X' characters in result.
            while j < n and result[j] == 'X':
                j += 1

            # One string ended while the other still has non-X characters.
            if i == n and j == n:
                return True
            if i == n or j == n:
                return False

            # The next non-X characters must match in both order and type.
            if start[i] != result[j]:
                return False

            # 'L' can only move left, so its final index cannot be greater
            # than its starting index. Here i is start index, j is result index.
            if start[i] == 'L' and i < j:
                return False

            # 'R' can only move right, so its final index cannot be smaller
            # than its starting index.
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True