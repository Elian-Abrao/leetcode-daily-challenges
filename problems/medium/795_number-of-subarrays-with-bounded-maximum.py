class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """
        Count subarrays where the maximum element lies in [left, right].
        Uses the identity:
            count(max in [L,R]) = count(max <= R) - count(max <= L-1).
        Subarrays with max <= X are those where every element <= X,
        which can be counted by scanning and tracking runs of valid elements.
        """
        # Helper: number of subarrays where all elements <= limit.
        def count_leq(limit: int) -> int:
            total = 0          # total count of valid subarrays
            run_len = 0        # length of current contiguous segment of elements <= limit
            for x in nums:
                if x <= limit:
                    run_len += 1
                    total += run_len   # each new element creates 'run_len' new subarrays
                else:
                    run_len = 0
            return total

        # Subarrays with max <= right  minus  those with max <= left-1.
        # left-1 may be negative; then count_leq returns 0 because all nums are >=0.
        return count_leq(right) - count_leq(left - 1)