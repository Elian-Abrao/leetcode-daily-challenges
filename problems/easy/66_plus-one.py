from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the least significant digit (end of the list)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # Increment current digit
            if digits[i] < 10:
                # If no carry is produced, we are done
                return digits
            # If digit becomes 10, set to 0 and propagate carry to next more significant digit
            digits[i] = 0
        # If we exited the loop, all digits were '9' and turned to '0', so we need an extra leading '1'
        return [1] + digits