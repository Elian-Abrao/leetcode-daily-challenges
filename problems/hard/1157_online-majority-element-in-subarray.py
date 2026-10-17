from __future__ import annotations
from collections import defaultdict
import random
import bisect


class MajorityChecker:
    """
    Design a data structure to quickly find majority elements in subarrays.
    
    Key idea: Since threshold always satisfies 2 * threshold > subarray_length,
    any valid majority element must also be a Boyer-Moore majority candidate.
    We combine:
      1. A segment tree with Boyer-Moore majority candidates and their counts.
      2. Precomputed position lists for each distinct value to verify candidates.
    """
    
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.arr = arr
        
        # Position lists: value -> sorted list of all indices where it appears.
        self.pos = defaultdict(list)
        for idx, val in enumerate(arr):
            self.pos[val].append(idx)
        
        # Build segment tree storing (candidate, count) pairs.
        # Count is the net Boyer-Moore count (not total frequency).
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [(0, 0)] * (2 * size)
        
        # Load leaves with actual values.
        for i in range(self.n):
            self.tree[size + i] = (arr[i], 1)
        
        # Build internal nodes bottom-up.
        for i in range(size - 1, 0, -1):
            left_idx = i << 1
            right_idx = left_idx | 1
            self.tree[i] = self._merge_node(self.tree[left_idx], self.tree[right_idx])
    
    def _merge_node(self, left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        """
        Merge two Boyer-Moore candidates from left and right halves.
        Returns combined (candidate, net_count).
        """
        cand_left, cnt_left = left
        cand_right, cnt_right = right
        
        if cand_left == cand_right:
            return (cand_left, cnt_left + cnt_right)
        
        # Different candidates: subtract counts, keep the one with larger net count.
        if cnt_left >= cnt_right:
            return (cand_left, cnt_left - cnt_right)
        else:
            return (cand_right, cnt_right - cnt_left)
    
    def _query_range(self, left: int, right: int) -> tuple[int, int]:
        """
        Query the segment tree for Boyer-Moore candidate in arr[left...right].
        Returns (candidate, net_count) — net_count is not directly usable.
        """
        l = left + self.size
        r = right + self.size
        
        # Collect all O(log n) segment candidates and merge them sequentially.
        l_nodes = []
        r_nodes = []
        
        while l <= r:
            if l & 1:
                l_nodes.append(self.tree[l])
                l += 1
            if not (r & 1):
                r_nodes.append(self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        
        # Merge collected nodes: first left-side nodes then right-side nodes reversed.
        all_nodes = l_nodes + r_nodes[::-1]
        if not all_nodes:
            return (0, 0)
        
        res = all_nodes[0]
        for node in all_nodes[1:]:
            res = self._merge_node(res, node)
        return res
    
    def query(self, left: int, right: int, threshold: int) -> int:
        """
        Return the element occurring at least 'threshold' times in 
        arr[left...right], or -1 if no such element exists.
        """
        # Boyer-Moore only gives a candidate, not verification.
        candidate, _ = self._query_range(left, right)
        if candidate == 0:
            return -1
        
        # Verify actual frequency using binary search on position list.
        positions = self.pos.get(candidate)
        if not positions:
            return -1
        
        # Count occurrences of candidate in [left, right].
        lo = bisect.bisect_left(positions, left)
        hi = bisect.bisect_right(positions, right)
        freq = hi - lo
        
        if freq >= threshold:
            return candidate
        return -1