from typing import List, Tuple

class MyCalendarTwo:
    """
    Calendar that allows booking events without causing a triple booking.
    Uses two lists: single bookings (events added once) and double bookings
    (times covered by exactly two events). A new event is rejected if it
    overlaps any existing double booking. Otherwise, overlaps with single
    bookings are added to the double list, and the event itself is recorded.
    """

    def __init__(self) -> None:
        # Intervals with exactly one booking.
        self.single: List[Tuple[int, int]] = []
        # Intervals with exactly two overlapping bookings.
        self.double: List[Tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        """
        Attempt to book an event [startTime, endTime).
        Returns True if successful (no triple booking), False otherwise.
        """
        # 1. Reject if the new interval intersects any double‑booked region.
        for d_start, d_end in self.double:
            if max(d_start, startTime) < min(d_end, endTime):
                return False

        # 2. For each existing single booking, compute the overlap with the
        #    new event. This overlapping part will become double‑booked.
        for s_start, s_end in self.single:
            overlap_start = max(s_start, startTime)
            overlap_end   = min(s_end, endTime)
            if overlap_start < overlap_end:
                self.double.append((overlap_start, overlap_end))

        # 3. Record the new event as a single booking.
        self.single.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)