class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Count uppercase letters to distinguish the three valid forms.
        uppercase_count = sum(1 for ch in word if ch.isupper())

        # Valid if all letters are uppercase, all are lowercase,
        # or only the first letter is uppercase.
        return (
            uppercase_count == len(word) or  # "USA"
            uppercase_count == 0 or           # "leetcode"
            (uppercase_count == 1 and word[0].isupper())  # "Google"
        )