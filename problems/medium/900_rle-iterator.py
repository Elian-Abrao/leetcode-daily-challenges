from typing import List

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.pos = 0  # index into encoding, points to the count of current run

    def next(self, n: int) -> int:
        last = -1

        # Skip zero-length runs at the current position
        while self.pos < len(self.encoding) and self.encoding[self.pos] == 0:
            self.pos += 2

        # Consume up to n elements from the remaining runs
        while n > 0 and self.pos < len(self.encoding):
            count = self.encoding[self.pos]
            val = self.encoding[self.pos + 1]

            if n <= count:
                # Exhaust part of the current run
                self.encoding[self.pos] -= n
                last = val
                n = 0
                if self.encoding[self.pos] == 0:
                    # Move to the next run if the current one is depleted
                    self.pos += 2
                    while self.pos < len(self.encoding) and self.encoding[self.pos] == 0:
                        self.pos += 2
                break
            else:
                # Exhaust the entire current run and continue
                n -= count
                last = val
                self.pos += 2
                # Skip any zero-length runs that may follow
                while self.pos < len(self.encoding) and self.encoding[self.pos] == 0:
                    self.pos += 2

        if n > 0:
            return -1
        return last