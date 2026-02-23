from __future__ import annotations
from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # Optional preprocessing: remove any word that is a substring of another word.
        # This is safe because the final superstring containing the larger word will
        # automatically contain the substring as well.
        words = self._filter_substrings(words)
        n = len(words)
        if n == 0:
            return ""

        # Precompute pairwise overlaps:
        # overlap[i][j] = maximum length k such that suffix of words[i] of length k
        # equals prefix of words[j] of length k.
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                maxk = min(len(a), len(b))
                for k in range(maxk, 0, -1):
                    if a.endswith(b[:k]):
                        overlap[i][j] = k
                        break

        size = 1 << n
        # DP[mask][i] stores the best superstring that uses the set 'mask'
        # and ends with word i.
        dp: List[List[str | None]] = [[None] * n for _ in range(size)]
        for i in range(n):
            dp[1 << i][i] = words[i]

        # Iterate all masks, try to append a new word j not in the mask.
        for mask in range(size):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                cur = dp[mask][i]
                if cur is None:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    nm = mask | (1 << j)
                    candidate = cur + words[j][overlap[i][j]:]
                    if dp[nm][j] is None or \
                       len(candidate) < len(dp[nm][j]) or \
                       (len(candidate) == len(dp[nm][j]) and candidate < dp[nm][j]):
                        dp[nm][j] = candidate

        full = size - 1
        best: str | None = None
        for i in range(n):
            s = dp[full][i]
            if s is None:
                continue
            if best is None or len(s) < len(best) or (len(s) == len(best) and s < best):
                best = s
        return best or ""

    def _filter_substrings(self, words: List[str]) -> List[str]:
        # Remove strings that are substrings of others to reduce DP state space.
        n = len(words)
        removed = [False] * n
        for i in range(n):
            if removed[i]:
                continue
            for j in range(n):
                if i == j or removed[j]:
                    continue
                wi, wj = words[i], words[j]
                # If wi is contained in wj, wi can be dropped safely.
                if len(wi) <= len(wj) and wi in wj:
                    removed[i] = True
                    break
        return [words[i] for i in range(n) if not removed[i]]