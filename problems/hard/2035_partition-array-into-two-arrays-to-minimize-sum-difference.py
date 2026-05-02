from typing import List
from itertools import combinations
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        target = total / 2  # Ideal sum for each partition
        
        # Split array into two halves
        left = nums[:n]
        right = nums[n:]
        
        # Generate all subset sums for each half, grouped by count
        def generate_subset_sums(arr):
            # sums[k] contains all possible sums using exactly k elements
            sums = [[] for _ in range(n + 1)]
            
            # Generate all subsets using bitmask
            for mask in range(1 << n):
                subset_sum = 0
                count = 0
                for i in range(n):
                    if mask & (1 << i):
                        subset_sum += arr[i]
                        count += 1
                sums[count].append(subset_sum)
            
            # Sort each group for binary search
            for k in range(n + 1):
                sums[k].sort()
            
            return sums
        
        left_sums = generate_subset_sums(left)
        right_sums = generate_subset_sums(right)
        
        min_diff = float('inf')
        
        # Try all possible ways to pick k from left and (n-k) from right
        for k in range(n + 1):
            # We need exactly n elements total
            # Pick k from left, need (n-k) from right
            need_from_right = n - k
            
            # For each sum from left with k elements
            for left_sum in left_sums[k]:
                # We want left_sum + right_sum = target
                # So right_sum should be close to (target - left_sum)
                desired_right = target - left_sum
                
                # Binary search in right_sums[need_from_right]
                right_list = right_sums[need_from_right]
                
                # Find closest value to desired_right
                idx = bisect_left(right_list, desired_right)
                
                # Check the value at idx and idx-1 (if exists)
                for check_idx in [idx, idx - 1]:
                    if 0 <= check_idx < len(right_list):
                        right_sum = right_list[check_idx]
                        sum1 = left_sum + right_sum
                        sum2 = total - sum1
                        diff = abs(sum1 - sum2)
                        min_diff = min(min_diff, diff)
        
        return min_diff