from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res