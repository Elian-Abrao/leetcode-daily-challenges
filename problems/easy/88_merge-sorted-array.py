from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Fill from the back so values in nums1 are never overwritten
        # before they have been compared.
        write = m + n - 1
        i = m - 1
        j = n - 1

        # If nums2 is empty, nums1 is already correct.
        if n == 0:
            return

        # While both arrays still have unmerged values, place the larger
        # one at the current write position to keep the result sorted.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                # Prefer nums2 on ties; either choice is valid for sorting.
                nums1[write] = nums2[j]
                j -= 1
            write -= 1

        # Only nums2 may still need copying. If nums1 has leftovers, they
        # are already in the correct place at the front.
        while j >= 0:
            nums1[write] = nums2[j]
            j -= 1
            write -= 1