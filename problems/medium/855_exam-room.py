from bisect import bisect_left, insort
from typing import List

class ExamRoom:
    """
    Simulates an exam room with seats 0..n-1.

    Uses a sorted list of occupied seats to compute the best seat for each
    incoming student. O(k) per seat() call, where k is the current number
    of occupied seats. With at most 10^4 calls, this is acceptable.
    """

    def __init__(self, n: int):
        self.n = n
        # Sorted list of currently occupied seat numbers.
        self.occupied: List[int] = []

    def seat(self) -> int:
        """Assign the next student to the seat that maximizes the distance
        to the closest occupied seat, with tie‑breaking by smallest number."""
        occ = self.occupied
        # Trivial case: no one in the room -> sit at 0.
        if not occ:
            insort(occ, 0)
            return 0

        best_seat = -1
        best_dist = -1

        # Segment from left boundary (virtual seat -1) to the first occupied seat.
        # Candidate seat is 0; distance = first occupied seat (since seat 0 to first).
        first = occ[0]
        if first > 0:
            seat = 0
            dist = first - 0          # distance to closest person (only the first)
            if dist > best_dist or (dist == best_dist and seat < best_seat):
                best_dist = dist
                best_seat = seat

        # Interior segments between consecutive occupied seats.
        for i in range(len(occ) - 1):
            l = occ[i]
            r = occ[i + 1]
            gap = r - l
            # The best seat inside an interior segment is the midpoint.
            seat = (l + r) // 2
            # Distance from the candidate seat to the closer occupied end.
            dist = min(seat - l, r - seat)
            if dist > best_dist or (dist == best_dist and seat < best_seat):
                best_dist = dist
                best_seat = seat

        # Segment from last occupied seat to right boundary (virtual seat n).
        last = occ[-1]
        if last < self.n - 1:
            seat = self.n - 1
            dist = (self.n - 1) - last
            if dist > best_dist or (dist == best_dist and seat < best_seat):
                best_dist = dist
                best_seat = seat

        # Insert the chosen seat and return it.
        insort(occ, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """Remove the student at seat p. It is guaranteed p is occupied."""
        occ = self.occupied
        idx = bisect_left(occ, p)
        # Since p is guaranteed to be in the list, idx is valid.
        occ.pop(idx)