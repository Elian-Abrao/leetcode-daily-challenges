from __future__ import annotations

class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        """
        Returns the sum of widths of all non-empty subsequences of nums.
        Width = max - min of the subsequence.
        
        Key insight: For any subsequence, its width depends only on its min and max.
        Sorting does not change the set of possible subsequences (since order doesn't 
        matter for min/max), and it greatly simplifies counting.
        
        After sorting, for each element at index i:
        - It acts as the maximum of a subsequence when all chosen elements are 
          from positions <= i, and it is included. That's 2^i subsequences.
        - It acts as the minimum of a subsequence when all chosen elements are 
          from positions >= i, and it is included. That's 2^(n-1-i) subsequences.
        
        Contribution of nums[i] as max minus as min gives net contribution = 
            nums[i] * (2^i - 2^(n-1-i))
        
        We sum over all i (mod 1e9+7).
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Sort so that min and max for subsequences can be determined by positions
        nums.sort()
        
        # Precompute powers of 2 modulo MOD up to n
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        total = 0
        for i in range(n):
            # Count of subsequences where nums[i] is the maximum
            as_max = pow2[i]  # 2^i
            # Count of subsequences where nums[i] is the minimum
            as_min = pow2[n - 1 - i]  # 2^(n-1-i)
            
            contribution = (nums[i] * (as_max - as_min)) % MOD
            total = (total + contribution) % MOD
        
        return total