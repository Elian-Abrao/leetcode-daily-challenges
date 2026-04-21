from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the list of characters in place using a two-pointer approach.
        - i starts at the beginning, j at the end.
        - Swap s[i] and s[j], then move pointers towards the center.
        - Time complexity: O(n), Space complexity: O(1).
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1