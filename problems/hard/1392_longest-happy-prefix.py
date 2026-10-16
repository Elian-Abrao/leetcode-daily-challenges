class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Returns the longest proper prefix of s that is also a suffix.
        If no such prefix exists, returns an empty string.
        """
        n = len(s)

        # Trivial case: single character cannot have a proper prefix that is a suffix.
        if n == 1:
            return ""

        # ---------- KMP prefix function (pi) ----------
        # pi[i] = length of the longest proper prefix of s[0..i]
        #          that is also a suffix of that substring.
        pi = [0] * n

        # Length of the current longest matched prefix which is also a suffix.
        prev = 0

        # Start from the second character (index 1) because pi[0] = 0 always.
        for i in range(1, n):
            # While there is a mismatch and we can fall back to a shorter match:
            while prev > 0 and s[i] != s[prev]:
                prev = pi[prev - 1]

            # If characters match, we can extend the matched length.
            if s[i] == s[prev]:
                prev += 1

            pi[i] = prev

        # The last element of pi gives the longest proper prefix of the whole string
        # that is also a suffix. This is exactly what we need.
        longest_len = pi[n - 1]
        return s[:longest_len]