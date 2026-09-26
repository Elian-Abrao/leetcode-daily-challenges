class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Returns the minimum number of operations to reduce n to 0,
        using the two allowed bit flips.
        
        The recurrence relation:
        Let hb be the highest power of 2 <= n.
        Then f(n) = (2*hb - 1) - f(n - hb) , with f(0) = 0.
        This is derived from the structure of the Gray code inversion
        induced by the allowed operations.
        """
        # Base case: zero requires zero operations
        if n == 0:
            return 0
        
        # Find the highest set bit: the largest power of two <= n
        highest_bit = 1 << (n.bit_length() - 1)
        
        # Apply the recurrence formula
        # (2 * highest_bit - 1) is the total number of steps needed to
        # clear the highest bit and return to zero when starting from
        # the pure power-of-two state.
        return (2 * highest_bit - 1) - self.minimumOneBitOperations(n - highest_bit)