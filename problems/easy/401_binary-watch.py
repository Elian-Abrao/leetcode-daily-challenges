from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Brute force approach: iterate through all valid hours and minutes
        # and check if the total number of bits set equals turnedOn
        
        result = []
        
        # Hours range from 0 to 11 (4 bits, but max value is 11)
        # Minutes range from 0 to 59 (6 bits, but max value is 59)
        for hour in range(12):
            for minute in range(60):
                # Count the number of 1 bits in both hour and minute
                # bin(x).count('1') counts the number of '1' characters in binary representation
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Format: hour without leading zero, minute with leading zero if needed
                    result.append(f"{hour}:{minute:02d}")
        
        return result