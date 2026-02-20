from __future__ import annotations
from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1:
            return len(s)

        def dfs(sub: str) -> int:
            if not sub:
                return 0
            freq = Counter(sub)
            for ch, cnt in freq.items():
                if cnt < k:
                    max_len = 0
                    i = 0
                    n = len(sub)
                    while i < n:
                        while i < n and sub[i] == ch:
                            i += 1
                        if i >= n:
                            break
                        j = i
                        while j < n and sub[j] != ch:
                            j += 1
                        max_len = max(max_len, dfs(sub[i:j]))
                        i = j
                    return max_len
            return len(sub)

        return dfs(s)