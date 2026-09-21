from __future__ import annotations

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        """
        Returns True if the array can become non-decreasing by modifying at most one element.
        A non-decreasing array satisfies nums[i] <= nums[i+1] for all i.
        """
        n = len(nums)
        # Trivial case: single element is always non-decreasing.
        if n <= 1:
            return True

        # Find the first index i where nums[i] > nums[i+1].
        violation_idx = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                # If we already found a violation, more than one -> impossible.
                if violation_idx != -1:
                    return False
                violation_idx = i

        # No violation found: already non-decreasing.
        if violation_idx == -1:
            return True

        i = violation_idx
        # Now we have exactly one violation at index i.
        # We can try to fix it by modifying either nums[i] or nums[i+1].

        # Option 1: Lower nums[i] so that it fits between nums[i-1] and nums[i+1].
        # This is possible when i == 0 (no left neighbour) or nums[i-1] <= nums[i+1].
        if i == 0 or nums[i - 1] <= nums[i + 1]:
            # After lowering nums[i], the array becomes non-decreasing.
            return True

        # Option 2: Raise nums[i+1] so that nums[i] <= nums[i+2] holds.
        # This works when i+1 is the last element or nums[i] <= nums[i+2].
        if i + 1 == n - 1 or nums[i] <= nums[i + 2]:
            # After raising nums[i+1], the array becomes non-decreasing.
            return True

        # Neither fix works -> impossible with only one modification.
        return False