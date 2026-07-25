from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        
        # Find the previous and next smaller elements for each index
        # These define the range where strength[i] is the minimum
        
        # prev_smaller[i]: index of previous element < strength[i], or -1
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        # next_smaller[i]: index of next element < strength[i], or n
        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        
        # Prefix sum array for quick range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD
        
        # Prefix of prefix sums for calculating sum of all subarray sums
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD
        
        result = 0
        
        # For each index i, calculate contribution when strength[i] is minimum
        for i in range(n):
            # Range where strength[i] is minimum: (left, right)
            left = prev_smaller[i]  # exclusive left boundary
            right = next_smaller[i]  # exclusive right boundary
            
            # Count of subarrays where i is minimum and includes position i
            # Left side: i can pair with indices from (left+1) to i
            # Right side: i can pair with indices from i to (right-1)
            
            # Number of positions on left: i - left
            # Number of positions on right: right - i
            left_count = i - left
            right_count = right - i
            
            # Calculate sum of all subarray sums where i is the minimum
            # For subarray [l, r] containing i:
            # sum[l, r] = prefix[r+1] - prefix[l]
            
            # We need: sum over all l in (left, i] and r in [i, right) of (prefix[r+1] - prefix[l])
            # = sum of prefix[r+1] terms - sum of prefix[l] terms
            
            # Sum of positive contribution (right endpoints)
            # For each r in [i, right), it appears in (i - left) subarrays
            # Sum = left_count * sum(prefix[i+1] to prefix[right])
            pos_contribution = 0
            for r in range(i, right):
                pos_contribution = (pos_contribution + prefix[r + 1]) % MOD
            pos_contribution = (pos_contribution * left_count) % MOD
            
            # Sum of negative contribution (left endpoints)
            # For each l in (left, i], it appears in (right - i) subarrays
            # Sum = right_count * sum(prefix[left+1] to prefix[i])
            neg_contribution = 0
            for l in range(left + 1, i + 1):
                neg_contribution = (neg_contribution + prefix[l]) % MOD
            neg_contribution = (neg_contribution * right_count) % MOD
            
            # Use prefix of prefix sums for O(1) calculation
            # Sum of prefix[i+1] to prefix[right] = prefix_prefix[right+1] - prefix_prefix[i+1]
            pos_sum = (prefix_prefix[right + 1] - prefix_prefix[i + 1]) % MOD
            pos_contribution = (left_count * pos_sum) % MOD
            
            # Sum of prefix[left+1] to prefix[i] = prefix_prefix[i+1] - prefix_prefix[left+1]
            neg_sum = (prefix_prefix[i + 1] - prefix_prefix[left + 1]) % MOD
            neg_contribution = (right_count * neg_sum) % MOD
            
            # Total sum contribution for subarrays with minimum at i
            total_sum = (pos_contribution - neg_contribution) % MOD
            
            # Multiply by minimum value strength[i]
            contribution = (strength[i] * total_sum) % MOD
            result = (result + contribution) % MOD
        
        return result