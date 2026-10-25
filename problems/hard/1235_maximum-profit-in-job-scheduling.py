from __future__ import annotations
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        # Combine jobs into tuples (end, start, profit) and sort by end time.
        jobs = sorted(zip(endTime, startTime, profit))  # sorts by first element (end)
        # Extract sorted end times for binary search.
        ends = [job[0] for job in jobs]
        # dp[i] = maximum profit considering first i jobs (sorted by end).
        dp = [0] * (n + 1)  # dp[0] = 0
        for i in range(1, n + 1):
            end, start, prof = jobs[i - 1]
            # Find the number of jobs whose end time <= current start time.
            # Since jobs are sorted by end, this is a prefix of the processed jobs.
            prev_count = bisect_right(ends, start)  # count of jobs with end <= start
            # Option 1: take current job and add best profit from compatible jobs
            take = prof + dp[prev_count]
            # Option 2: skip current job
            skip = dp[i - 1]
            # Store the better of the two
            dp[i] = take if take > skip else skip
        return dp[n]