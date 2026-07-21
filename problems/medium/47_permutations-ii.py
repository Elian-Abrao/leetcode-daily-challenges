from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort to group duplicates together, enabling skip logic
        nums.sort()
        result = []
        n = len(nums)
        used = [False] * n
        
        def backtrack(path):
            # Base case: we've built a complete permutation
            if len(path) == n:
                result.append(path[:])
                return
            
            for i in range(n):
                # Skip if already used in current path
                if used[i]:
                    continue
                
                # Skip duplicate elements at same recursion level:
                # If current element equals previous and previous not used,
                # it means we already explored this branch with the previous occurrence.
                # This ensures we only use duplicates in sorted order (left to right).
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Choose current element
                path.append(nums[i])
                used[i] = True
                
                # Recurse
                backtrack(path)
                
                # Unchoose (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([])
        return result