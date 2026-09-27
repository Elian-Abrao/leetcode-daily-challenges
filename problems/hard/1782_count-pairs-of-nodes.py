class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        # 1-indexed degree array
        deg = [0] * (n + 1)
        # count of multiple edges between the same pair (undirected)
        edge_cnt = {}  # key = (min_node, max_node)

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            # normalise to smaller index first
            if u > v:
                u, v = v, u
            key = (u, v)
            edge_cnt[key] = edge_cnt.get(key, 0) + 1

        # sorted degrees for the two‑pointer part
        deg_list = [deg[i] for i in range(1, n + 1)]
        deg_list.sort()
        total_pairs = n * (n - 1) // 2

        ans = []
        for q in queries:
            # ----- count pairs with deg[a] + deg[b] > q -----
            # two pointers: count pairs with sum <= q
            cnt_le = 0
            j = n - 1
            for i in range(n):
                # move j leftwards because deg_list is sorted increasingly
                while j > i and deg_list[i] + deg_list[j] > q:
                    j -= 1
                if j > i:
                    cnt_le += (j - i)
            cnt_gt = total_pairs - cnt_le

            # ----- remove pairs whose incident value actually <= q -----
            # incident(a,b) = deg[a] + deg[b] - cnt(a,b)
            # these pairs were counted in cnt_gt but fail the strict > q condition
            for (a, b), c in edge_cnt.items():
                s = deg[a] + deg[b]
                if s > q and s - c <= q:   # incident <= q → should be excluded
                    cnt_gt -= 1

            ans.append(cnt_gt)

        return ans