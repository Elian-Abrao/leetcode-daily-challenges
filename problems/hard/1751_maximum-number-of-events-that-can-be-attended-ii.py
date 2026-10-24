from bisect import bisect_left

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        # Sort events by their end day (weighted interval scheduling pattern)
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Pre‑extract sorted end days for binary search
        ends = [e[1] for e in events]

        # dp_prev[i] = maximum total value using at most (current_event_count)
        # events among the first i events.  Initially 0 events allowed.
        dp_prev = [0] * (n + 1)

        # Gradually allow up to k events
        for _ in range(k):
            dp_cur = [0] * (n + 1)
            # Process events in order of increasing end day
            for i, (s, _, v) in enumerate(events, start=1):
                # Number of events that end strictly before s (non‑overlapping)
                p = bisect_left(ends, s)
                # Best if we attend current event (combine with one fewer event)
                take = v + dp_prev[p]
                # Best if we skip current event
                dp_cur[i] = max(dp_cur[i - 1], take)
            dp_prev = dp_cur

        # After allowing up to k events, we have the answer
        return dp_prev[n]