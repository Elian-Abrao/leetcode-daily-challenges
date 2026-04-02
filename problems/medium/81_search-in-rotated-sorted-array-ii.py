from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Standard binary search on a rotated array works unless duplicates
        # hide which half is sorted. In that ambiguous case, shrink the window.
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Immediate hit keeps the common case fast.
            if nums[mid] == target:
                return True

            # When both ends equal the middle, we cannot determine the sorted side.
            # Removing both ends is safe because nums[mid] is already known != target.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # If the left half is sorted, target must lie inside its value range
            # to justify searching there; otherwise it must be on the other side.
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Otherwise the right half is sorted, so use the symmetric check.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # The window is exhausted, so target does not exist in the array.
        return False