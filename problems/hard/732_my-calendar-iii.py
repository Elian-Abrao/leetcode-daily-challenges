from __future__ import annotations
from bisect import bisect_left
from typing import List, Tuple

class MyCalendarThree:
    """
    Tracks the maximum number of concurrent events (k-booking) after each booking.
    Uses a sweep-line approach with a difference array stored as a sorted list of
    (time, delta) pairs.  At most 400 calls, so O(N) per operation is sufficient.
    """

    def __init__(self) -> None:
        # Sorted list of (time, delta) representing changes in active event count.
        self._events: List[Tuple[int, int]] = []

    def _add_delta(self, time: int, delta: int) -> None:
        """
        Insert a delta (usually +1 for start, -1 for end) into the sorted event list.
        If an entry for the exact time already exists, combine the deltas.
        """
        idx = bisect_left(self._events, (time,))  # compare only by time
        if idx < len(self._events) and self._events[idx][0] == time:
            # Combine deltas for the same time
            old_delta = self._events[idx][1]
            self._events[idx] = (time, old_delta + delta)
        else:
            # Insert new entry at the correct position
            self._events.insert(idx, (time, delta))

    def book(self, startTime: int, endTime: int) -> int:
        """
        Adds a new event [startTime, endTime) and returns the maximum number of
        concurrent events after this booking.
        """
        # Record start (+1) and end (-1) in the difference array
        self._add_delta(startTime, 1)
        self._add_delta(endTime, -1)

        # Sweep through all events in chronological order to find peak concurrency
        current = 0
        max_concurrent = 0
        for _, delta in self._events:
            current += delta
            if current > max_concurrent:
                max_concurrent = current

        return max_concurrent