class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Determine if the string can be made a palindrome by deleting at most one character.
        Uses a two-pointer approach. On first mismatch, we try skipping either the left
        or right character and verify if the remaining substring is a palindrome.
        """
        n = len(s)

        def is_pal_range(l: int, r: int) -> bool:
            """
            Check if s[l..r] is a palindrome.
            """
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        i, j = 0, n - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # Either skip the left character or skip the right character
                return is_pal_range(i + 1, j) or is_pal_range(i, j - 1)
        return True