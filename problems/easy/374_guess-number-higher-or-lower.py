# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Binary search to find the picked number in range [1, n]
        # Time: O(log n), Space: O(1)
        
        left, right = 1, n
        
        while left <= right:
            # Use mid = left + (right - left) // 2 to avoid potential overflow
            # (though Python handles big integers natively, this is best practice)
            mid = left + (right - left) // 2
            
            result = guess(mid)
            
            if result == 0:
                # Found the correct number
                return mid
            elif result == -1:
                # Our guess is too high, search lower half
                right = mid - 1
            else:  # result == 1
                # Our guess is too low, search upper half
                left = mid + 1
        
        # Should never reach here given problem constraints guarantee pick exists in [1, n]
        return -1