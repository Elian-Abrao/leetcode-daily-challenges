class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # The minimum possible speed is 1, maximum is the largest pile.
        # Any speed larger than max(piles) results in the same total hours (number of piles),
        # so the answer lies in [1, max(piles)].
        left, right = 1, max(piles)

        # Helper to compute total hours needed for a given speed k.
        # Returns True if total hours <= h, i.e., feasible.
        def feasible(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                # ceil division without floating point: (pile + k - 1) // k
                total_hours += (pile + k - 1) // k
                # Early exit: if already exceeded h, no need to continue.
                if total_hours > h:
                    return False
            return True

        # Binary search for the minimal k.
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                # mid works, try smaller speed (shift right boundary down)
                right = mid
            else:
                # mid too slow, need larger speed
                left = mid + 1

        # left == right, the minimal feasible speed.
        return left