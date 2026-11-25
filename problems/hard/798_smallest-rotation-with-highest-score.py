class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        # diff array of size n+1 for easy handling of intervals that may end at n-1
        diff = [0] * (n + 1)

        # Process each element: determine the rotation indices k where it scores.
        # The element at index i with value a scores iff (i - k) mod n >= a.
        # This is equivalent to k belonging to the circular interval
        #   [ start = (i+1)%n , end = (i-a)%n ] inclusive.
        # (Proof: the complement is a contiguous block of length a.)
        for i, a in enumerate(nums):
            start = (i + 1) % n
            end = (i - a) % n

            # Add +1 to the whole circular interval [start, end] using diff.
            if start <= end:
                # Interval does not wrap around.
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                # Interval wraps: split into [start, n-1] and [0, end].
                diff[start] += 1
                diff[n] -= 1          # sentinel, not used in final prefix sum
                diff[0] += 1
                diff[end + 1] -= 1

        # Compute prefix sums to obtain score for each k.
        cur = 0
        best_k = 0
        best_score = -1
        for k in range(n):
            cur += diff[k]
            # Update when strictly larger score (tie → keep smaller k)
            if cur > best_score:
                best_score = cur
                best_k = k

        return best_k