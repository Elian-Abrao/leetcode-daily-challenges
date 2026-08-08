class MyCalendar:

    def __init__(self):
        # Store booked intervals as a sorted list of (start, end) tuples
        # Maintaining sorted order allows for efficient conflict detection
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Two intervals [s1, e1) and [s2, e2) overlap if:
        # s1 < e2 AND s2 < e1
        # Equivalently, they DON'T overlap if: e1 <= s2 OR e2 <= s1
        
        # Check for conflicts with existing bookings
        for start, end in self.bookings:
            # If new booking overlaps with existing booking, reject it
            if startTime < end and start < endTime:
                return False
        
        # No conflicts found, add the new booking
        # Insert in sorted order by start time for potential future optimizations
        # Using binary search insertion point to maintain sorted order
        import bisect
        bisect.insort(self.bookings, (startTime, endTime))
        return True