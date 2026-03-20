from typing import List
from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        windows = []
        pos_to_windows = [[] for _ in range(n)]
        queue = deque()
        done = [False] * n
        ans = []

        for i in range(n - m + 1):
            made = set()
            todo = set()
            for j in range(m):
                if target[i + j] == stamp[j]:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            windows.append((made, todo))
            if not todo:
                ans.append(i)
                for k in range(i, i + m):
                    if not done[k]:
                        done[k] = True
                        queue.append(k)
            else:
                for k in todo:
                    pos_to_windows[k].append(i)

        while queue:
            i = queue.popleft()
            for w in pos_to_windows[i]:
                made, todo = windows[w]
                if i in todo:
                    todo.remove(i)
                    if not todo:
                        ans.append(w)
                        for k in made:
                            if not done[k]:
                                done[k] = True
                                queue.append(k)

        if not all(done):
            return []

        return ans[::-1]