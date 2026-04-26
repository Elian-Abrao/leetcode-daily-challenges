from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize result array with n+1 zeros
        ans = [0] * (n + 1)
        
        # Dynamic programming approach using bit manipulation insight:
        # For any number i, we can relate it to i >> 1 (i divided by 2)
        # - If i is even: ans[i] = ans[i >> 1] (same number of 1s as i/2)
        # - If i is odd: ans[i] = ans[i >> 1] + 1 (one more 1 than i/2)
        # This works because right-shifting removes the least significant bit,
        # and we add 1 if that bit was a 1 (i.e., i is odd)
        
        for i in range(1, n + 1):
            # ans[i >> 1] gives us the count for i with LSB removed
            # i & 1 adds 1 if the LSB of i is 1 (i.e., i is odd)
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans