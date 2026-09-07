class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the characters in each word of the input string,
        preserving whitespace and word order.

        Approach:
        - Split the string by spaces to obtain individual words.
        - Reverse each word using slicing.
        - Join the reversed words with a single space.

        Complexity:
        - Time: O(n) where n is the length of the string.
        - Space: O(n) for the output list and the split strings.
        """
        # Split the string into words (single space separation is guaranteed)
        words = s.split()
        # Reverse each word and join back with spaces
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)