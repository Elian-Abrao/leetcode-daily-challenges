class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Key insight: When we AND a range of consecutive numbers, any bit position
        # that flips from 0 to 1 (or 1 to 0) within the range will result in 0.
        # Only the common prefix bits that don't change across the range survive.
        
        # Example: [5, 7] = [101, 110, 111]
        # 101 & 110 & 111 = 100
        # The rightmost bits flip, only the common prefix "10x" → "100" remains.
        
        # Strategy: Find the common prefix by right-shifting both numbers
        # until they become equal. Then shift back to restore position.
        
        shift = 0
        
        # Keep shifting right until left and right converge to the same value
        # This finds the longest common prefix in their binary representations
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift back to restore the common prefix to its original position
        # All bits that were shifted away are 0 in the result (they varied in the range)
        return left << shift