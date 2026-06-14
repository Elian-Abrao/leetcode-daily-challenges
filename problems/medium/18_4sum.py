from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort to enable two-pointer technique and easy duplicate skipping
        nums.sort()
        n = len(nums)
        result = []
        
        # Edge case: need at least 4 elements
        if n < 4:
            return result
        
        # Fix first element
        for i in range(n - 3):
            # Skip duplicate first elements to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if smallest possible sum with current i exceeds target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            # Skip if largest possible sum with current i is less than target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            
            # Fix second element
            for j in range(i + 1, n - 2):
                # Skip duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Early termination for second loop
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                
                # Skip if largest possible sum with current i, j is less than target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # Two-pointer approach for remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Skip duplicates for fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers after finding a valid quadruplet
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        # Need larger sum, move left pointer right
                        left += 1
                    else:
                        # Need smaller sum, move right pointer left
                        right -= 1
        
        return result