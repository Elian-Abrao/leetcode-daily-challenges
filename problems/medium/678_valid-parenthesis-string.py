class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Greedy approach using a range of possible open parenthesis counts.
        - low: minimum possible number of unmatched '(' (by treating '*' as ')' or empty)
        - high: maximum possible number of unmatched '(' (by treating '*' as '(' )
        At each step, adjust bounds. If high becomes negative, invalid.
        At the end, low must be 0 for a valid string.
        Time: O(n), Space: O(1)
        """
        low = 0   # minimal possible open parentheses
        high = 0  # maximal possible open parentheses

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                # * as ')' reduces low; * as '(' increases high
                low -= 1
                high += 1

            # If high < 0, too many ')', even with all '*' as '(' we cannot match
            if high < 0:
                return False

            # low cannot be negative; we can always discard some '*' as empty
            if low < 0:
                low = 0

        # At the end, low must be 0 meaning all '(' can be matched
        return low == 0