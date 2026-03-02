from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Implements regex matching with '.' and '*':
        - '.' matches any single character.
        - '*' matches zero or more of the preceding element.
        The function returns True if the entire string s matches the pattern p.
        """
        n, m = len(s), len(p)

        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            # If we've reached end of the pattern, s must also be exhausted
            if j == m:
                return i == n

            # Check if the current characters (if any) match
            first_match = (i < n) and (p[j] == s[i] or p[j] == '.')

            # If the next character in pattern is '*', we have two choices:
            # 1) Treat '*' as zero occurrences -> skip the current element and '*'
            # 2) If current chars match, consume one char in s and keep the same pattern (since '*' can repeat)
            if (j + 1) < m and p[j + 1] == '*':
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Regular single-character match and move both pointers
                return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)