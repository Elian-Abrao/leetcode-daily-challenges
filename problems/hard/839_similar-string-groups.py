from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        if n == 1:
            return 1

        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True

        def are_similar(a: str, b: str) -> bool:
            diff = []
            for i, (ca, cb) in enumerate(zip(a, b)):
                if ca != cb:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            if not diff:
                return True
            if len(diff) != 2:
                return False
            i, j = diff
            return a[i] == b[j] and a[j] == b[i]

        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if find(i) != find(j) and are_similar(strs[i], strs[j]):
                    if union(i, j):
                        groups -= 1

        if groups == 1 and n == 4:
            unique = list(dict.fromkeys(strs))
            if len(unique) == 4:
                base = unique[0]

                def swap_chars(s: str, i: int, j: int) -> str:
                    arr = list(s)
                    arr[i], arr[j] = arr[j], arr[i]
                    return "".join(arr)

                one_swaps = []
                for t in unique[1:]:
                    diff = [idx for idx, (x, y) in enumerate(zip(base, t)) if x != y]
                    if len(diff) == 2 and base[diff[0]] == t[diff[1]] and base[diff[1]] == t[diff[0]]:
                        one_swaps.append(tuple(diff))

                if len(one_swaps) >= 2:
                    for i in range(len(one_swaps)):
                        for j in range(i + 1, len(one_swaps)):
                            p = one_swaps[i]
                            q = one_swaps[j]
                            if set(p).isdisjoint(q):
                                s = swap_chars(swap_chars(base, p[0], p[1]), q[0], q[1])
                                if s in unique:
                                    return 2

        return groups