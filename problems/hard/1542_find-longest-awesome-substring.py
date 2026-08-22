class Solution:
    def longestAwesome(self, s: str) -> int:
        # Bitmask representing parity (0 = even, 1 = odd) for digits 0-9.
        # We want longest substring where mask has at most one 1-bit.
        # Use dictionary to store earliest index for each mask.
        first_occurrence = {0: -1}  # empty prefix before index 0
        curr_mask = 0
        max_len = 0

        for i, ch in enumerate(s):
            digit = ord(ch) - 48          # '0' -> 0, '1' -> 1, ...
            curr_mask ^= (1 << digit)    # flip parity of this digit

            # Case 1: all counts even (mask = 0)
            # This substring from first occurrence of curr_mask to i is even-only.
            if curr_mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[curr_mask])

            # Case 2: exactly one digit has odd count (mask is a power of two)
            for d in range(10):
                candidate = curr_mask ^ (1 << d)
                if candidate in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[candidate])

            # Store first occurrence of this mask if not already present
            if curr_mask not in first_occurrence:
                first_occurrence[curr_mask] = i

        return max_len