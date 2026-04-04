# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search is optimal here because versions are monotonic:
        # once a version is bad, every later version is also bad.
        left, right = 1, n

        # Keep shrinking until both pointers meet at the first bad version.
        while left < right:
            # This midpoint formula is safe in languages with fixed-width ints,
            # and is a good habit even though Python integers do not overflow.
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid could still be the first bad version, so keep it.
                right = mid
            else:
                # mid is definitely good, so the answer must be after it.
                left = mid + 1

        # left == right, and by invariant it points to the first bad version.
        return left