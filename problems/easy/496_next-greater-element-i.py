from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map each value in nums2 to its next greater value.
        # Because values are unique, the value itself is a safe dictionary key.
        next_greater = {}

        # Monotonic decreasing stack of values whose next greater element
        # has not been found yet.
        stack = []

        for value in nums2:
            # Any smaller value on the stack has found its first greater
            # element at the current value.
            while stack and stack[-1] < value:
                next_greater[stack.pop()] = value

            # Keep unresolved values for future elements to match against.
            stack.append(value)

        # Remaining values have no greater element to their right.
        while stack:
            next_greater[stack.pop()] = -1

        # Answer queries from nums1 in O(1) each using the precomputed map.
        return [next_greater[value] for value in nums1]