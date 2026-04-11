from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # If there are more workers than jobs, each worker can take at most one job.
        # The answer is simply the maximum single job time.
        if k >= len(jobs):
            return max(jobs) if jobs else 0

        # Sort jobs in descending order to fail faster in infeasible branches.
        jobs.sort(reverse=True)

        # Feasibility check: can we assign jobs so that no worker exceeds 'limit'?
        def can(limit: int) -> bool:
            # Quick rejection: if the heaviest job exceeds the limit, impossible.
            if jobs[0] > limit:
                return False

            # Current accumulated time for each worker.
            sums = [0] * k
            n = len(jobs)

            def dfs(index: int) -> bool:
                if index == n:
                    # All jobs assigned successfully within limit.
                    return True
                x = jobs[index]

                # To avoid duplicating work for workers with identical sums,
                # track seen sums we've already tried for this job.
                seen = set()
                for i in range(k):
                    if sums[i] + x <= limit and sums[i] not in seen:
                        seen.add(sums[i])
                        sums[i] += x
                        if dfs(index + 1):
                            return True
                        sums[i] -= x
                    # If this worker bin is empty (0) and we failed with it,
                    # there's no need to try other empty bins (symmetry pruning).
                    if sums[i] == 0:
                        break
                return False

            return dfs(0)

        # Binary search the minimal feasible maximum working time.
        low, high = max(jobs), sum(jobs)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans