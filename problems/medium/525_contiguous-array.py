from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Finds the maximum length of a contiguous subarray with equal number of 0s and 1s.
        
        Approach:
        - Treat 0 as -1 and 1 as +1 to transform the problem into finding the longest
          subarray with sum 0.
        - Use prefix sums and a hashmap to store the first occurrence of each prefix sum.
        - When the same prefix sum appears again, the subarray between the two indices
          has net sum 0 → equal number of 0s and 1s.
        
        Time: O(n) single pass
        Space: O(n) for the hashmap (worst-case n+1 distinct sums)
        """
        # Map prefix sum -> earliest index where this sum occurred.
        # Initialize with sum 0 at index -1 to handle subarrays starting from index 0.
        first_occurrence = {0: -1}
        
        max_length = 0
        current_sum = 0
        
        for i, val in enumerate(nums):
            # Convert: 0 -> -1, 1 -> +1
            current_sum += -1 if val == 0 else 1
            
            if current_sum in first_occurrence:
                # Subarray from (first_occurrence[current_sum] + 1) to i has equal 0s and 1s.
                subarray_length = i - first_occurrence[current_sum]
                if subarray_length > max_length:
                    max_length = subarray_length
            else:
                # Store only the first occurrence to maximize subarray length later.
                first_occurrence[current_sum] = i
        
        return max_length