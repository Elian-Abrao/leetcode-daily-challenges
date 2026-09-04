from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        Repeatedly merge adjacent non-coprime numbers by replacing them with their LCM.
        Since merging order does not affect the final result, we can process greedily
        from left to right using a stack-like approach.
        """
        stack: List[int] = []
        
        for num in nums:
            # Push current number onto the stack.
            stack.append(num)
            
            # While the stack has at least two elements and the top two are non-coprime,
            # merge them: pop the top, compute LCM with the new top, and push back.
            # Reasoning: merging right away is safe because any future merges involving
            # the merged result will still be possible; the process converges to the same
            # final array regardless of order.
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break  # coprime, cannot merge
                # Replace the two numbers with their LCM.
                # Compute LCM via a // g * b to avoid overflow in intermediate product.
                lcm = a // g * b
                # Pop the last element (b), then replace the new top (a) with lcm.
                stack.pop()
                stack[-1] = lcm
        
        return stack