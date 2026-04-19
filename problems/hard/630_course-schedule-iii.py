from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Schedule the maximum number of courses using a greedy approach.

        Key idea:
        - Sort courses by their last permissible day (deadline) ascending.
        - Maintain a max-heap (via negative durations) of durations of chosen courses.
        - Keep a running total_time of all chosen durations.
        - If total_time exceeds the current course's deadline, remove the longest duration
          course taken so far to free up time. This preserves feasibility for all
          previously considered courses (since they had earlier deadlines).
        - The size of the heap at the end is the maximum number of courses we can take.

        Complexity:
        - Sorting: O(n log n)
        - Each course is pushed once and possibly popped once: O(n log n)
        - Overall: O(n log n) time, O(n) extra space due to the heap.
        """
        if not courses:
            return 0

        # Sort by lastDay to ensure feasibility constraints are checked in order
        courses.sort(key=lambda c: c[1])

        max_heap = []  # store durations as negative values to simulate a max-heap
        total_time = 0

        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)

            # If current total_time exceeds the current course's deadline, drop the longest course
            if total_time > last_day:
                longest = -heapq.heappop(max_heap)
                total_time -= longest

        # The number of courses in the heap is the maximum feasible count
        return len(max_heap)