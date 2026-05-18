class Solution:
    def findComplement(self, num: int) -> int:
        # Find the position of the most significant bit (MSB)
        # This tells us how many bits are actually used in the number
        # For example: 5 = 101 has 3 bits, so bit_length = 3
        bit_length = num.bit_length()
        
        # Create a mask with all 1s for the length of num's binary representation
        # For num = 5 (101), bit_length = 3, so mask = 111 = 7
        # Formula: 2^bit_length - 1 gives us all 1s in those positions
        mask = (1 << bit_length) - 1
        
        # XOR num with mask to flip all bits in the relevant positions
        # Example: 5 (101) XOR 7 (111) = 2 (010)
        # XOR flips each bit: 1^1=0, 0^1=1
        return num ^ mask