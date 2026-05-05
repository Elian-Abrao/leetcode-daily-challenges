from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to enable pruning and systematic exploration
        candidates.sort()
        
        result = []
        
        def backtrack(start: int, current: List[int], remaining: int):
            # Base case: found a valid combination
            if remaining == 0:
                result.append(current[:])  # Make a copy of current combination
                return
            
            # Base case: overshoot target (pruning)
            if remaining < 0:
                return
            
            # Explore candidates starting from 'start' index
            # This prevents duplicate combinations (e.g., [2,3] and [3,2])
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                
                # Early termination: if current candidate exceeds remaining,
                # all subsequent candidates (being sorted) will also exceed
                if candidate > remaining:
                    break
                
                # Include current candidate and explore further
                current.append(candidate)
                
                # Recurse with same start index 'i' to allow reuse of same candidate
                backtrack(i, current, remaining - candidate)
                
                # Backtrack: remove last added candidate to try next option
                current.pop()
        
        # Start backtracking from index 0, empty combination, full target
        backtrack(0, [], target)
        
        return result