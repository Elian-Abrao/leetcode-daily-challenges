class Solution:
    def hammingWeight(self, n: int) -> int:
        # Count the number of set bits (1s) in the binary representation of n
        # Using Brian Kernighan's algorithm: n & (n-1) clears the rightmost set bit
        # This is efficient when the number of set bits is small
        # Time: O(k) where k is the number of set bits, Space: O(1)
        
        count = 0
        
        # Each iteration clears one set bit from n
        # Loop terminates when all set bits are cleared (n becomes 0)
        while n:
            n &= n - 1  # Clear the rightmost set bit
            count += 1
        
        return count