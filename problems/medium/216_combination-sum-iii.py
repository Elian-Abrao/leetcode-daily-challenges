from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        # Early termination: check if target sum is achievable with k distinct numbers from 1-9
        # Minimum sum with k numbers: 1+2+...+k = k*(k+1)/2
        # Maximum sum with k numbers: (10-k)+(10-k+1)+...+9 = k*(19-k)/2
        min_sum = k * (k + 1) // 2
        max_sum = k * (19 - k) // 2
        if n < min_sum or n > max_sum:
            return result
        
        def backtrack(start: int, current: List[int], remaining_sum: int, remaining_count: int):
            # Base case: found valid combination
            if remaining_count == 0 and remaining_sum == 0:
                result.append(current[:])  # Copy current combination
                return
            
            # Pruning: stop if we can't complete a valid combination
            if remaining_count == 0 or remaining_sum <= 0:
                return
            
            # Try each number from start to 9
            for num in range(start, 10):
                # Pruning: if current number already exceeds remaining sum, no point continuing
                if num > remaining_sum:
                    break
                
                # Additional pruning: check if we can reach the target with remaining slots
                # We need at least remaining_count numbers, and the minimum sum would be
                # num + (num+1) + ... for remaining_count numbers
                # If even the minimum exceeds our budget, skip
                min_possible = remaining_count * num + (remaining_count * (remaining_count - 1)) // 2
                if min_possible > remaining_sum:
                    break
                
                # Choose current number
                current.append(num)
                
                # Recurse with next number (num+1 to avoid reuse), reduced sum and count
                backtrack(num + 1, current, remaining_sum - num, remaining_count - 1)
                
                # Backtrack: remove current number to try next option
                current.pop()
        
        backtrack(1, [], n, k)
        return result