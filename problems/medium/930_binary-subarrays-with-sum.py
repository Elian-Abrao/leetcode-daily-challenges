class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Count subarrays with sum equal to goal using prefix sum and hashmap.
        
        Key insight: For any subarray [j..i], sum = prefix[i+1] - prefix[j].
        We count how many prefix sums equal the current prefix sum minus goal.
        
        Time: O(n), Space: O(n) for the hashmap.
        """
        from collections import defaultdict
        
        # Handle edge case: empty array would have no subarrays
        if not nums:
            return 0
        
        # Hashmap to store frequency of each prefix sum seen so far
        # Initially, prefix sum 0 has occurred once (empty prefix)
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        
        current_sum = 0  # Running prefix sum
        total_subarrays = 0
        
        for num in nums:
            # Update the running prefix sum
            current_sum += num
            
            # A subarray ends at current index with sum = goal
            # if there exists a previous prefix sum = current_sum - goal.
            # The count of such previous prefixes gives the number of valid subarrays
            # ending at this position.
            needed_prefix = current_sum - goal
            if needed_prefix in prefix_counts:
                total_subarrays += prefix_counts[needed_prefix]
            
            # Record the current prefix sum for future subarrays
            prefix_counts[current_sum] += 1
        
        return total_subarrays