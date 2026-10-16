class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        Count good numbers in [1, n]. A number is good if after rotating each digit
        individually (0->0,1->1,8->8, 2<->5, 6<->9) the result is valid and different.
        Valid digits are {0,1,2,5,6,8,9}; to be different the number must contain at
        least one digit from {2,5,6,9}.

        Time: O(n * log10(n)) ≈ 4*10^4 operations for n ≤ 10^4.
        Space: O(1).
        """
        def is_good(x: int) -> bool:
            s = str(x)
            has_change = False
            for ch in s:
                # If any invalid digit appears, rotation fails immediately.
                if ch in ('3', '4', '7'):
                    return False
                # Digits that cause a change (map to a different digit).
                if ch in ('2', '5', '6', '9'):
                    has_change = True
            # All digits are valid; good if at least one change occurred.
            return has_change

        count = 0
        for i in range(1, n + 1):
            if is_good(i):
                count += 1
        return count