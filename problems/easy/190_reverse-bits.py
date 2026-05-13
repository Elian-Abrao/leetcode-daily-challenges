class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result to accumulate reversed bits
        result = 0
        
        # Process all 32 bits of the input integer
        # We iterate exactly 32 times since we're dealing with 32-bit integers
        for i in range(32):
            # Extract the least significant bit (LSB) from n
            bit = n & 1
            
            # Shift result left to make room for the new bit
            # Then OR with the extracted bit to place it at LSB of result
            result = (result << 1) | bit
            
            # Shift n right to process the next bit in the next iteration
            n >>= 1
        
        return result