from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max_subsequence(nums: List[int], length: int) -> List[int]:
            # Monotonic stack: keep the lexicographically largest subsequence
            # while preserving order and removing exactly len(nums) - length digits.
            if length == 0:
                return []

            drops = len(nums) - length
            stack: List[int] = []

            for digit in nums:
                # Remove smaller previous digits when we can still fill the target length later.
                while drops and stack and stack[-1] < digit:
                    stack.pop()
                    drops -= 1
                stack.append(digit)

            # Extra digits, if any, must be removed from the tail.
            return stack[:length]

        def greater_suffix(a: List[int], i: int, b: List[int], j: int) -> bool:
            # Compare remaining suffixes lexicographically.
            # Needed during merge when current digits tie.
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            if j == len(b):
                return True
            if i == len(a):
                return False
            return a[i] > b[j]

        def merge(a: List[int], b: List[int]) -> List[int]:
            # Greedily take from the sequence with the larger remaining suffix.
            i = 0
            j = 0
            merged: List[int] = []

            while i < len(a) or j < len(b):
                if greater_suffix(a, i, b, j):
                    merged.append(a[i])
                    i += 1
                else:
                    merged.append(b[j])
                    j += 1

            return merged

        m, n = len(nums1), len(nums2)

        # The split must be feasible for both arrays.
        start = max(0, k - n)
        end = min(k, m)

        best: List[int] = []

        for take1 in range(start, end + 1):
            take2 = k - take1

            part1 = pick_max_subsequence(nums1, take1)
            part2 = pick_max_subsequence(nums2, take2)
            candidate = merge(part1, part2)

            # Lexicographic comparison on lists matches the problem's ordering goal.
            if candidate > best:
                best = candidate

        return best