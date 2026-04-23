class Solution:
    def toHex(self, num: int) -> str:
        # Handle the zero edge case explicitly
        if num == 0:
            return "0"
        
        # Hexadecimal digits for mapping 0..15 to '0'..'f'
        hex_digits = "0123456789abcdef"
        
        # For negative numbers, interpret as 32-bit unsigned using two's complement
        # This emulates (num + 2^32) for negative values, and leaves positives unchanged.
        unsigned = num & 0xFFFFFFFF
        
        # Build hex representation from least significant nibble to most significant
        parts = []
        while unsigned:
            nibble = unsigned & 0xF
            parts.append(hex_digits[nibble])
            unsigned >>= 4  # Move to the next 4 bits
        
        # The digits are collected in reverse order
        return ''.join(reversed(parts))