from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log n) requirement suggests binary search approach
        # We need to find leftmost and rightmost positions of target
        
        # Handle empty array edge case
        if not nums:
            return [-1, -1]
        
        # Find leftmost (first) occurrence of target
        left_pos = self._find_left_bound(nums, target)
        
        # If target not found, return [-1, -1]
        if left_pos == -1:
            return [-1, -1]
        
        # Find rightmost (last) occurrence of target
        right_pos = self._find_right_bound(nums, target)
        
        return [left_pos, right_pos]
    
    def _find_left_bound(self, nums: List[int], target: int) -> int:
        """
        Binary search to find the leftmost position of target.
        Returns -1 if target not found.
        """
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                # Found target, but continue searching left half
                # to find the leftmost occurrence
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                # Target must be in right half
                left = mid + 1
            else:
                # nums[mid] > target, search left half
                right = mid - 1
        
        return result
    
    def _find_right_bound(self, nums: List[int], target: int) -> int:
        """
        Binary search to find the rightmost position of target.
        Assumes target exists in array (called only after left bound found).
        """
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                # Found target, but continue searching right half
                # to find the rightmost occurrence
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                # Target must be in right half
                left = mid + 1
            else:
                # nums[mid] > target, search left half
                right = mid - 1
        
        return result