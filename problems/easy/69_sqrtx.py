class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: sqrt(0) = 0, sqrt(1) = 1
        if x < 2:
            return x
        
        # Binary search for the floor of square root
        # Search space: [1, x] but we can optimize upper bound to x // 2 + 1
        # because for x >= 2, sqrt(x) <= x // 2
        left, right = 1, x // 2
        
        # Invariant: answer is in [left, right]
        # We're looking for largest integer k where k * k <= x
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == x:
                # Exact square root found
                return mid
            elif square < x:
                # mid could be the answer, but check if there's a larger one
                # Move left boundary up
                left = mid + 1
            else:
                # square > x, so mid is too large
                # Move right boundary down
                right = mid - 1
        
        # When loop exits, right < left
        # right is the largest integer where right * right <= x
        # left is the smallest integer where left * left > x
        return right