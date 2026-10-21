class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        # Pair difficulties with profits and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers to process them in increasing ability order
        workers = sorted(worker)
        total = 0          # accumulated maximum profit
        best = 0           # best profit seen so far (for difficulty ≤ current worker)
        idx = 0            # index into the sorted jobs list

        for ability in workers:
            # Include all jobs that this worker (and all later workers) can do
            while idx < len(jobs) and jobs[idx][0] <= ability:
                best = max(best, jobs[idx][1])
                idx += 1
            # best is now the maximum profit for any job this worker can take
            total += best

        return total