from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Generate Gray code using the formula: gray(i) = i XOR (i >> 1)
        # This converts binary counting sequence to Gray code
        # where each successive value differs by exactly one bit
        
        # Total numbers in n-bit Gray code sequence
        size = 1 << n  # 2^n
        
        result = []
        for i in range(size):
            # Apply Gray code formula: XOR the number with its right shift
            # This ensures adjacent codes differ by one bit
            gray = i ^ (i >> 1)
            result.append(gray)
        
        return result