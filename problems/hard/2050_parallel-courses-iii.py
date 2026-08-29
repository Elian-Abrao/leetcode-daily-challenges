from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build adjacency list and indegree array.
        # Use 0-indexed courses for internal representation.
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for prev, nxt in relations:
            prev -= 1  # convert to 0-indexed
            nxt -= 1   # convert to 0-indexed
            graph[prev].append(nxt)
            indegree[nxt] += 1
        
        # dp[i] = earliest completion time for course i (months)
        # Start with the time needed for the course itself.
        dp = time[:]  # copy, since time is 0-indexed already
        
        # Initialize queue with all courses having no prerequisites.
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        # Topological sort (Kahn's algorithm) to process courses in order.
        while queue:
            course = queue.popleft()
            # For each dependent course, update its earliest completion time.
            for next_course in graph[course]:
                # The earliest start for next_course is at least dp[course]
                # because course must be completed first.
                # We take the max over all prerequisites.
                # dp[next_course] already includes its own time,
                # so we only need to consider the prerequisite's completion.
                # Use a temporary variable to avoid overwriting the base time incorrectly.
                # Actually, dp[next_course] currently holds time[next_course] (its own time).
                # The earliest start for next_course is max over all prereq completions.
                # So we need to add its own time to that max.
                # We store intermediate: earliest start = max(dp[prereq]) for all prereq,
                # then dp[next_course] = max(dp[next_course], earliest_start + time[next_course])
                # Since we haven't added its own time yet, we compute:
                # earliest_start_for_next = dp[course]  (the time when this prereq finishes)
                # The overall completion for next is:
                # max(current dp[next_course], earliest_start_for_next + time[next_course])
                # But dp[next_course] currently holds only its own time, which is the minimum
                # if started at 0. We need to add the max prerequisite time to it.
                # Easiest: compute candidate = dp[course] + time[next_course]
                if dp[course] + time[next_course] > dp[next_course]:
                    dp[next_course] = dp[course] + time[next_course]
                
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        # The answer is the maximum completion time among all courses.
        return max(dp)