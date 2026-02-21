from __future__ import annotations
from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # quick lookup
        n = len(s)
        if n == 0:
            return [""]
        max_len = max((len(w) for w in wordDict), default=0)

        # dp[i] will be True if s[i:] can be segmented into dictionary words
        dp = [False] * (n + 1)
        dp[n] = True  # empty string is a valid end

        # Build dp from right to left to know feasible cut points
        for i in range(n - 1, -1, -1):
            end_max = min(n, i + max_len)
            for j in range(i + 1, end_max + 1):
                if s[i:j] in word_set and dp[j]:
                    dp[i] = True
                    break

        if not dp[0]:
            return []  # no possible sentence

        @lru_cache(None)
        def dfs(start: int) -> List[str]:
            if start == n:
                return [""]  # base: end of string yields empty suffix
            res: List[str] = []
            end_max = min(n, start + max_len)
            for end in range(start + 1, end_max + 1):
                word = s[start:end]
                if word in word_set and dp[end]:
                    suffixes = dfs(end)
                    for suf in suffixes:
                        if suf == "":
                            res.append(word)
                        else:
                            res.append(word + " " + suf)
            return res

        return dfs(0)