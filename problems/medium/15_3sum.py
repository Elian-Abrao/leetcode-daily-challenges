class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to enable two-pointer technique and easy duplicate skipping
        nums.sort()
        result = []
        n = len(nums)
        
        # Iterate through array, treating each element as potential first element of triplet
        for i in range(n - 2):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if smallest element is positive, no valid triplet exists
            if nums[i] > 0:
                break
            
            # Use two pointers to find pairs that sum to -nums[i]
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                    
                elif current_sum < target:
                    # Sum too small, need larger values, move left pointer right
                    left += 1
                else:
                    # Sum too large, need smaller values, move right pointer left
                    right -= 1
        
        return result