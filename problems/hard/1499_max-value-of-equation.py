from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        """
        Maximise y_i + y_j + |x_i - x_j| with |x_i - x_j| <= k and i < j.
        Since x_i < x_j, |x_i - x_j| = x_j - x_i.
        Expression = (y_i - x_i) + (y_j + x_j).
        For each j we need max of (y_i - x_i) among i < j with x_j - x_i <= k.
        Use a deque to maintain a sliding window of valid i, ordered by decreasing (y_i - x_i).
        """
        # Deque stores indices with strictly decreasing (y_i - x_i)
        dq = deque()
        n = len(points)
        # Problem guarantees at least one valid pair, but we initialise to very small value.
        ans = -10**18

        for j in range(n):
            xj, yj = points[j]
            # Remove points from front that are outside the x-difference window
            while dq and xj - points[dq[0]][0] > k:
                dq.popleft()

            # If there is any valid i, compute candidate answer
            if dq:
                i = dq[0]
                xi, yi = points[i]
                # value_i = yi - xi, value_j = yj + xj
                candidate = (yi - xi) + (yj + xj)
                if candidate > ans:
                    ans = candidate

            # Insert current point j into deque, maintaining decreasing order of (yj - xj)
            # Since we only care about future j' > j, we keep larger values near front.
            val_j = yj - xj
            while dq:
                # Compare value at back with val_j
                last = dq[-1]
                x_last, y_last = points[last]
                if (y_last - x_last) <= val_j:
                    dq.pop()
                else:
                    break
            dq.append(j)

        return ans