from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to enable two-pointer approach
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with a value that will definitely be replaced
        # Using first three elements as initial candidate
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through array, fixing first element of triplet
        for i in range(n - 2):
            # Use two pointers for remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found exact target, return immediately (can't get closer)
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on whether sum is too small or too large
                if current_sum < target:
                    # Need larger sum, move left pointer right
                    left += 1
                else:
                    # Need smaller sum, move right pointer left
                    right -= 1
        
        return closest_sum