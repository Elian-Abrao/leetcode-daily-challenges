from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # Not enough jobs to fill each day with at least one job.
        if d > n:
            return -1

        # Precompute max difficulty for every subarray [l, r] (inclusive).
        # max_diff[l][r] = max(jobDifficulty[l..r])
        max_diff = [[0] * n for _ in range(n)]
        for i in range(n):
            cur_max = jobDifficulty[i]
            for j in range(i, n):
                cur_max = max(cur_max, jobDifficulty[j])
                max_diff[i][j] = cur_max

        # dp[days][jobs] = min total difficulty to schedule first 'jobs' jobs (1-indexed)
        # in exactly 'days' days.
        INF = 10 ** 9
        dp = [[INF] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0  # 0 jobs in 0 days has 0 difficulty

        for day in range(1, d + 1):
            # We need at least 'day' jobs: start from 'day' because each day needs one job.
            for jobs in range(day, n + 1):
                # Try splitting at position k: last day covers jobs k+1 .. jobs (1-indexed).
                # k is the number of jobs scheduled before the last day.
                # k must be at least day-1 (previous days need one job each) and at most jobs-1.
                best = INF
                # Iterate k from day-1 to jobs-1 (inclusive).
                # The last day's difficulty is max of jobDifficulty[k..jobs-1].
                for k in range(day - 1, jobs):
                    # Difficulty of last day = max_diff[k][jobs-1] using 0-indexed indices.
                    prev = dp[day - 1][k]
                    if prev != INF:
                        last_day_difficulty = max_diff[k][jobs - 1]
                        total = prev + last_day_difficulty
                        if total < best:
                            best = total
                dp[day][jobs] = best

        return dp[d][n]