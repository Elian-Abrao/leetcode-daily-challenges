from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        For each element not yet visited, traverse the cycle it belongs to.
        The permutation property ensures each element starts a unique cycle,
        so we can mark visited elements in-place (negation) to avoid extra space.
        """
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            # Skip already visited elements (negative marks visited)
            if nums[i] < 0:
                continue
            
            # Start a new cycle from nums[i]
            cur_len = 0
            idx = i
            
            # Walk the cycle until we hit a visited element
            while nums[idx] >= 0:
                # Mark current element as visited by negating it
                # Since values are in [0, n-1], we can safely negate
                next_idx = nums[idx]
                nums[idx] = -1  # mark visited
                idx = next_idx
                cur_len += 1
                
                # If we wrapped back to a visited element, this cycle is done
            
            # Update global maximum
            if cur_len > max_len:
                max_len = cur_len
                
            # Early exit: no need to continue if we already found the largest possible cycle
            # (maximum cycle length is bounded by n, but we can still check remaining small cycles)
            # This is optional; the algorithm is O(n) anyway.
        
        return max_len