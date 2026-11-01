class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Greedy ordering: sort by (minimum - actual) descending.
        # This minimises the maximum over tasks of (minimum + sum of actuals before it),
        # which is the required initial energy (exchange argument).
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

        total_actual = 0   # cumulative actual cost of processed tasks
        min_initial = 0    # answer

        for actual, minimum in tasks:
            # To start this task we need: initial >= minimum + total_actual_before
            min_initial = max(min_initial, total_actual + minimum)
            total_actual += actual

        return min_initial