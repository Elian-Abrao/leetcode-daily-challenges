from __future__ import annotations
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min((len(s) for s in strs), default=0)
        if min_len == 0:
            return ""
        for i in range(min_len):
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] != ch:
                    return strs[0][:i]
        return strs[0][:min_len]