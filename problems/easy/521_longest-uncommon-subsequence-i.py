class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If strings are identical, no uncommon subsequence exists.
        # Every subsequence of a is also a subsequence of b, and vice versa.
        if a == b:
            return -1
        
        # If strings differ, the longer string cannot be a subsequence
        # of the shorter one (unless equal, which we already ruled out).
        # Therefore, the longer string is an uncommon subsequence,
        # and its full length is the maximum possible answer.
        return max(len(a), len(b))