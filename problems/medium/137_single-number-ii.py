from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Count each bit position independently.
        # Bits contributed by numbers appearing three times cancel out modulo 3,
        # so the remaining bits reconstruct the unique number.
        result = 0

        # The constraints fit in signed 32-bit integers, so checking 32 bits is enough.
        for bit in range(32):
            bit_count = 0
            mask = 1 << bit

            for num in nums:
                # Python keeps infinite sign bits for negatives, but masking with a
                # finite 32-bit position still gives the correct contribution here.
                if num & mask:
                    bit_count += 1

            # If this bit survives modulo 3, it belongs to the answer.
            if bit_count % 3:
                result |= mask

        # If the sign bit is set, interpret the 32-bit pattern as a negative number.
        # This converts values like 0xFFFFFFFF back to -1.
        if result >= 1 << 31:
            result -= 1 << 32

        return result