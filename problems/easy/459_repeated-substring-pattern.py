class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Trivial check for very short strings
        if not s or len(s) == 1:
            return False
        # Core trick: if s can be formed by repeating a substring,
        # then s will appear in (s + s) with its first and last chars removed.
        ss = s + s
        return s in ss[1:-1]