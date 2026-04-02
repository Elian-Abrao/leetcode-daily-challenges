class Solution:
    def addDigits(self, num: int) -> int:
        # Digital root property:
        # - 0 stays 0
        # - any positive number maps to 1..9 based on modulo 9
        # This gives O(1) time and avoids repeated digit summation.
        if num == 0:
            return 0
        
        # For multiples of 9, the digital root is 9 instead of 0.
        return 1 + (num - 1) % 9