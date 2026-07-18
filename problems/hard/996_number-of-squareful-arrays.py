from typing import List
from collections import Counter
import math

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # Check if sum of two numbers is a perfect square
        def is_perfect_square(n):
            if n < 0:
                return False
            root = int(math.sqrt(n))
            return root * root == n
        
        # Count frequency of each unique number to handle duplicates
        counter = Counter(nums)
        unique_nums = list(counter.keys())
        n = len(unique_nums)
        
        # Build adjacency graph: two numbers are adjacent if their sum is a perfect square
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if is_perfect_square(unique_nums[i] + unique_nums[j]):
                    graph[i].append(j)
        
        # DFS with backtracking to count valid permutations
        # remaining: how many numbers we still need to place
        def dfs(last_idx, remaining):
            # Base case: placed all numbers successfully
            if remaining == 0:
                return 1
            
            count = 0
            # Try each unique number that can follow the last number
            for next_idx in graph[last_idx]:
                # Only use if we still have this number available
                if counter[unique_nums[next_idx]] > 0:
                    # Use this number
                    counter[unique_nums[next_idx]] -= 1
                    count += dfs(next_idx, remaining - 1)
                    # Backtrack
                    counter[unique_nums[next_idx]] += 1
            
            return count
        
        result = 0
        # Try starting with each unique number
        for i in range(n):
            # Use this number as the first element
            counter[unique_nums[i]] -= 1
            result += dfs(i, len(nums) - 1)
            # Backtrack
            counter[unique_nums[i]] += 1
        
        return result