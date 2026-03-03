from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        Validate whether the given sequence of integers (each representing a byte)
        forms a valid UTF-8 encoding.

        Approach:
        - Maintain 'remaining' as the number of continuation bytes expected for the current character.
        - When remaining == 0, inspect the current byte:
          - If the most significant bit is 0 -> 1-byte character; continue.
          - Otherwise, count the number of leading '1' bits to determine total bytes of the character.
            - Valid leading counts are 2, 3, or 4. A leading '1' count of 1 is invalid (must start a continuation sequence).
            - Set remaining = leading - 1.
        - If remaining > 0, the current byte must start with '10' (i.e., (byte & 0xC0) == 0x80).
        - At the end, remaining must be 0.
        """
        remaining = 0  # number of continuation bytes expected after a leading byte

        for byte in data:
            b = byte & 0xFF  # ensure 8-bit value

            if remaining == 0:
                # Check if this is a 1-byte character (starts with 0)
                if (b & 0x80) == 0:
                    continue

                # Count the number of leading '1' bits to determine total bytes
                leading = 0
                mask = 0x80  # 10000000
                while (b & mask) != 0:
                    leading += 1
                    mask >>= 1
                    if mask == 0:
                        break

                # Leading 1s:
                # - 2, 3, or 4 indicate a multi-byte character
                # - 1 or >4 are invalid per UTF-8 rules
                if leading == 1 or leading > 4:
                    return False

                remaining = leading - 1
            else:
                # We are inside a multi-byte character; this byte must be a continuation byte
                if (b & 0xC0) != 0x80:
                    return False
                remaining -= 1

        # All bytes processed; ensure there is no unfinished multi-byte character
        return remaining == 0