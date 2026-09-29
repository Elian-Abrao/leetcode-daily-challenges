class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Perform binary search on a sorted array of unique integers.
        Returns the index of target if found, otherwise -1.
        """
        # Edge case: empty array (though constraints guarantee length >= 1)
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        # Standard binary search loop.
        # Invariant: target is in [left, right] if it exists.
        while left <= right:
            # Use mid = left + (right - left) // 2 to avoid overflow.
            # Python handles big ints, but this is a good practice.
            mid = left + (right - left) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val < target:
                # Discard left half, including mid.
                left = mid + 1
            else:
                # Discard right half, including mid.
                right = mid - 1

        # Target not found.
        return -1