from __future__ import annotations
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Fenwick Tree (Binary Indexed Tree) to maintain available servers
        class BIT:
            def __init__(self, n: int):
                self.n = n
                self.tree = [0] * (n + 1)

            def add(self, idx: int, delta: int) -> None:
                i = idx + 1
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & -i

            def sum(self, idx: int) -> int:
                """prefix sum from 0 to idx inclusive"""
                if idx < 0:
                    return 0
                i = idx + 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

            def total(self) -> int:
                return self.sum(self.n - 1)

            def find_kth(self, k: int) -> int:
                """return smallest index (0‑based) such that prefix sum >= k (1‑based)"""
                idx = 0
                bit_mask = 1 << (self.n.bit_length())
                while bit_mask:
                    t = idx + bit_mask
                    if t <= self.n and self.tree[t] < k:
                        idx = t
                        k -= self.tree[t]
                    bit_mask >>= 1
                return idx

        # Min‑heap of (finish_time, server_id) for busy servers
        busy = []

        # BIT storing available servers (1 = free, 0 = busy)
        available = BIT(k)
        for s in range(k):
            available.add(s, 1)

        # Count of handled requests per server
        handled = [0] * k

        for i, (arr_time, duration) in enumerate(zip(arrival, load)):
            # Free all servers that have finished by this arrival time
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id, 1)

            # If no server is free, drop the request
            if available.total() == 0:
                continue

            # Preferred server is i % k
            preferred = i % k
            # number of available servers with index < preferred
            cnt_before = available.sum(preferred - 1)
            total_avail = available.total()

            if total_avail > cnt_before:
                # There is at least one available server >= preferred
                server_id = available.find_kth(cnt_before + 1)
            else:
                # Wrap around to the first available server
                server_id = available.find_kth(1)

            # Assign this server
            available.add(server_id, -1)
            handled[server_id] += 1
            heapq.heappush(busy, (arr_time + duration, server_id))

        # Determine the maximum number of requests handled
        max_handled = max(handled)
        return [sid for sid, cnt in enumerate(handled) if cnt == max_handled]