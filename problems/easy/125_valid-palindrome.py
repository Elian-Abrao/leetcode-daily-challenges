class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if string s is a palindrome after removing non-alphanumeric
        characters and converting to lowercase, using a two-pointer approach.
        Time: O(n), Space: O(1)
        """
        i, j = 0, len(s) - 1

        while i < j:
            # Move i forward to the next alphanumeric character
            while i < j and not s[i].isalnum():
                i += 1
            # Move j backward to the previous alphanumeric character
            while i < j and not s[j].isalnum():
                j -= 1

            # After skipping non-alphanumeric, compare characters case-insensitively
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True