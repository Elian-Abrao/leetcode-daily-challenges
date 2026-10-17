from __future__ import annotations
import bisect
from typing import List


class Fenwick:
    """Fenwick tree (Binary Indexed Tree) for point updates and prefix sums.
    Also supports finding the smallest index with a given cumulative sum (order statistic)."""

    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int = 1) -> None:
        """Add delta at position idx (1‑based)."""
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        """Prefix sum 1 … idx (1‑based)."""
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def find_kth(self, k: int) -> int:
        """Return the smallest 1‑based index such that prefix sum >= k.
        Assumes 1 <= k <= total number of elements."""
        idx = 0
        # highest power of two not larger than n
        bitmask = 1 << (self.n.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1
        return idx + 1


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # compress room ids
        ids = sorted({r[0] for r in rooms})
        comp = {rid: i + 1 for i, rid in enumerate(ids)}  # 1‑based for Fenwick
        m = len(ids)

        # sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])

        # attach original index to queries, then sort by minSize descending
        qlist = [(pref, minsz, idx) for idx, (pref, minsz) in enumerate(queries)]
        qlist.sort(key=lambda x: -x[1])

        fen = Fenwick(m)
        ans = [-1] * len(queries)
        ptr = 0  # pointer over rooms

        for pref, minsz, qidx in qlist:
            # add all rooms with size >= current minSize
            while ptr < len(rooms) and rooms[ptr][1] >= minsz:
                fen.add(comp[rooms[ptr][0]])
                ptr += 1

            total = fen.sum(m)
            if total == 0:
                continue  # ans[qidx] already -1

            # binary search on compressed ids to find candidates around preferred
            pos = bisect.bisect_left(ids, pref)

            # predecessor: largest id <= pref
            pred_rank = None
            if pos > 0:
                limit = comp[ids[pos - 1]]
                cnt = fen.sum(limit)
                if cnt > 0:
                    pred_rank = fen.find_kth(cnt)

            # successor: smallest id >= pref
            succ_rank = None
            if pos < len(ids):
                limit = comp[ids[pos]]
                cnt_before = fen.sum(limit - 1)
                if cnt_before < total:
                    succ_rank = fen.find_kth(cnt_before + 1)

            # choose the best candidate
            best_id = None
            best_diff = None

            if pred_rank is not None:
                cand = ids[pred_rank - 1]
                diff = abs(cand - pref)
                best_id = cand
                best_diff = diff

            if succ_rank is not None:
                cand = ids[succ_rank - 1]
                diff = abs(cand - pref)
                if best_id is None or diff < best_diff or (diff == best_diff and cand < best_id):
                    best_id = cand
                    best_diff = diff

            ans[qidx] = best_id if best_id is not None else -1

        return ans