class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Use binary search to find if there exists an integer x such that x * x == num
        # Search space: [1, num], but we can optimize upper bound to num (or num // 2 + 1 for num > 1)
        
        # Edge case: num == 1 is a perfect square (1 * 1 = 1)
        if num == 1:
            return True
        
        # Binary search in range [1, num // 2]
        # For num >= 2, the square root is always <= num // 2
        # e.g., sqrt(4) = 2 = 4 // 2, sqrt(16) = 4 < 16 // 2 = 8
        left, right = 1, num // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            
            if square == num:
                # Found exact match
                return True
            elif square < num:
                # Need larger value
                left = mid + 1
            else:
                # square > num, need smaller value
                right = mid - 1
        
        # No integer found whose square equals num
        return False