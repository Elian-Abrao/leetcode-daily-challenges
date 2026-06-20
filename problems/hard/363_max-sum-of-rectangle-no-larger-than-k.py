from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # We reduce 2D problem to 1D by fixing top and bottom rows
        # For each column range, we compute cumulative sums and find
        # the maximum subarray sum <= k using a sorted list approach
        
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        # Optimize by iterating over the smaller dimension
        # If rows > cols, iterate over column pairs; otherwise row pairs
        if m > n:
            # More rows than columns: fix left and right columns
            for left in range(n):
                # row_sums[i] = sum of elements in row i from column left to right
                row_sums = [0] * m
                
                for right in range(left, n):
                    # Extend the column range to include column 'right'
                    for i in range(m):
                        row_sums[i] += matrix[i][right]
                    
                    # Now we have a 1D array (row_sums), find max subarray sum <= k
                    max_sum = max(max_sum, self._max_subarray_sum_no_larger_than_k(row_sums, k))
                    
                    # Early exit if we found exact match
                    if max_sum == k:
                        return k
        else:
            # More columns than rows (or equal): fix top and bottom rows
            for top in range(m):
                # col_sums[j] = sum of elements in column j from row top to bottom
                col_sums = [0] * n
                
                for bottom in range(top, m):
                    # Extend the row range to include row 'bottom'
                    for j in range(n):
                        col_sums[j] += matrix[bottom][j]
                    
                    # Now we have a 1D array (col_sums), find max subarray sum <= k
                    max_sum = max(max_sum, self._max_subarray_sum_no_larger_than_k(col_sums, k))
                    
                    # Early exit if we found exact match
                    if max_sum == k:
                        return k
        
        return max_sum
    
    def _max_subarray_sum_no_larger_than_k(self, arr: List[int], k: int) -> int:
        # Find maximum subarray sum in arr such that sum <= k
        # Using prefix sums and binary search with sorted list
        # 
        # For subarray [i+1, j], sum = prefix[j] - prefix[i]
        # We want prefix[j] - prefix[i] <= k
        # => prefix[i] >= prefix[j] - k
        # 
        # For each j, we find the smallest prefix[i] >= prefix[j] - k
        # in the set of all prefix sums seen so far (i < j)
        
        max_sum = float('-inf')
        prefix_sum = 0
        # Maintain sorted list of prefix sums
        sorted_prefix = [0]  # prefix sum before any element is 0
        
        for num in arr:
            prefix_sum += num
            
            # Find the smallest prefix in sorted_prefix that is >= prefix_sum - k
            target = prefix_sum - k
            idx = bisect_left(sorted_prefix, target)
            
            # If we found such a prefix, calculate the subarray sum
            if idx < len(sorted_prefix):
                max_sum = max(max_sum, prefix_sum - sorted_prefix[idx])
            
            # Insert current prefix_sum into sorted list for future queries
            insort(sorted_prefix, prefix_sum)
        
        return max_sum