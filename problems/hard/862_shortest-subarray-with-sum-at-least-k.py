from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Build prefix sums: prefix[i] = sum of nums[0..i-1]
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Deque will store indices of prefix sums in increasing order of the sums.
        # This monotonic property helps us efficiently find the best left bound.
        dq = deque()
        INF = 10 ** 9 + 7
        ans = INF

        for i in range(n + 1):
            # While the leftmost index can form a valid subarray ending at i,
            # update answer and remove it (since any later i can only yield longer subarray with that left bound).
            while dq and prefix[i] - prefix[dq[0]] >= k:
                length = i - dq.popleft()
                if length < ans:
                    ans = length

            # Maintain increasing order of prefix sums in deque.
            # If prefix at new index i is <= prefix at the back, the back index is
            # dominated (larger sum, older) and can be removed.
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        return ans if ans != INF else -1