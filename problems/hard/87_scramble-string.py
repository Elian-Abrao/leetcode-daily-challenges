from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        if s1 == s2:
            return True

        def sameChars(i1: int, i2: int, length: int) -> bool:
            # Check if the two substrings have the same multiset of characters.
            cnt = [0] * 26
            for k in range(length):
                cnt[ord(s1[i1 + k]) - 97] += 1
                cnt[ord(s2[i2 + k]) - 97] -= 1
            for v in cnt:
                if v != 0:
                    return False
            return True

        @lru_cache(maxsize=None)
        def dfs(i1: int, i2: int, length: int) -> bool:
            # Substring s1[i1:i1+length], s2[i2:i2+length]
            if length == 1:
                return s1[i1] == s2[i2]

            # Prune if character counts differ
            if not sameChars(i1, i2, length):
                return False

            # If substrings are already equal, it's a scramble
            if s1[i1:i1 + length] == s2[i2:i2 + length]:
                return True

            # Try all possible split points
            for split in range(1, length):
                # Case 1: no swap
                if dfs(i1, i2, split) and dfs(i1 + split, i2 + split, length - split):
                    return True
                # Case 2: swapped
                if dfs(i1, i2 + length - split, split) and dfs(i1 + split, i2, length - split):
                    return True
            return False

        return dfs(0, 0, n)