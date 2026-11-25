class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Uses two-pointer technique to simulate typing verification.
        Time: O(N + M) where N, M are lengths of name and typed.
        Space: O(1).
        """
        i, j = 0, 0          # i -> name index, j -> typed index
        n_len, t_len = len(name), len(typed)

        while i < n_len and j < t_len:
            # Current characters must match; otherwise, invalid.
            if name[i] != typed[j]:
                return False

            # Count consecutive occurrences in name
            name_char = name[i]
            name_count = 0
            while i < n_len and name[i] == name_char:
                name_count += 1
                i += 1

            # Count consecutive occurrences in typed
            typed_count = 0
            while j < t_len and typed[j] == name_char:
                typed_count += 1
                j += 1

            # typed must have at least as many of this character as name
            if typed_count < name_count:
                return False

        # Both pointers must be exhausted; no extra characters allowed.
        return i == n_len and j == t_len