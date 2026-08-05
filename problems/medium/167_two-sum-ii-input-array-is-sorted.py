from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers approach to leverage the sorted property
        # Time: O(n), Space: O(1)
        
        left = 0
        right = len(numbers) - 1
        
        # Since exactly one solution exists, we will always find it
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions as required
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum too small, move left pointer right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer left to decrease sum
                right -= 1
        
        # Should never reach here given problem guarantees
        return []