from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np_ = len(s), len(p)
        if np_ == 0 or np_ > ns:
            return []
        res: List[int] = []
        def idx(ch: str) -> int:
            return ord(ch) - 97
        cnts = [0]*26
        cntp = [0]*26
        for ch in p:
            cntp[idx(ch)] += 1
        for i in range(np_):
            cnts[idx(s[i])] += 1
        if cnts == cntp:
            res.append(0)
        for i in range(np_, ns):
            cnts[idx(s[i])] += 1
            cnts[idx(s[i-np_])] -= 1
            if cnts == cntp:
                res.append(i - np_ + 1)
        return res