class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        merged = []
        i = 0
        n = len(self.intervals)

        while i < n and self.intervals[i][1] < left:
            merged.append(self.intervals[i])
            i += 1

        new_left, new_right = left, right
        while i < n and self.intervals[i][0] <= new_right:
            new_left = min(new_left, self.intervals[i][0])
            new_right = max(new_right, self.intervals[i][1])
            i += 1
        merged.append([new_left, new_right])

        while i < n:
            merged.append(self.intervals[i])
            i += 1

        self.intervals = merged

    def queryRange(self, left: int, right: int) -> bool:
        intervals = self.intervals
        lo, hi = 0, len(intervals) - 1
        idx = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if intervals[mid][0] <= left:
                idx = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return idx != -1 and intervals[idx][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        updated = []

        for start, end in self.intervals:
            if end <= left or start >= right:
                updated.append([start, end])
            else:
                if start < left:
                    updated.append([start, left])
                if end > right:
                    updated.append([right, end])

        self.intervals = updated


Solution = RangeModule