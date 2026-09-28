class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Converts all uppercase letters in the string to lowercase.
        Time: O(n) where n = len(s)
        Space: O(n) for new string
        """
        # Use Python's built-in str.lower() which is optimized and clear.
        # Internally it handles ASCII and Unicode uppercase mapping.
        return s.lower()