class Solution:
    def maxGeneticDifference(self, parents: list[int], queries: list[list[int]]) -> list[int]:
        n = len(parents)
        # Build children adjacency list and locate root
        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Determine number of bits needed to represent all values
        max_val = 0
        for i in range(n):          # node values are their indices
            max_val = max(max_val, i)
        for node, val in queries:
            max_val = max(max_val, val)
        B = max_val.bit_length()
        if B == 0:                  # all values are zero
            B = 1

        # Group queries by the node they are attached to
        q_by_node = [[] for _ in range(n)]
        for idx, (node, val) in enumerate(queries):
            q_by_node[node].append((val, idx))

        ans = [0] * len(queries)

        # Binary trie: each node = [child0, child1, count]
        trie = [[-1, -1, 0]]        # index 0 is the root

        def insert(x: int) -> None:
            """Insert integer x into the trie."""
            node = 0
            trie[node][2] += 1
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                if trie[node][bit] == -1:
                    trie[node][bit] = len(trie)
                    trie.append([-1, -1, 0])
                node = trie[node][bit]
                trie[node][2] += 1

        def remove(x: int) -> None:
            """Remove integer x from the trie (assumes it was inserted once)."""
            node = 0
            trie[node][2] -= 1
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                nxt = trie[node][bit]
                trie[nxt][2] -= 1
                node = nxt

        def max_xor(x: int) -> int:
            """Return the maximum XOR of x with any integer currently in the trie."""
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                opp = 1 - bit
                # Try to take the opposite bit if available (and count > 0)
                if trie[node][opp] != -1 and trie[trie[node][opp]][2] > 0:
                    res |= (1 << b)
                    node = trie[node][opp]
                else:
                    node = trie[node][bit]   # same bit must exist (since count > 0)
            return res

        import sys
        sys.setrecursionlimit(200000)

        def dfs(u: int) -> None:
            """DFS from node u, maintaining a trie of all nodes on the current path."""
            insert(u)                  # add current node to the path
            for val, idx in q_by_node[u]:
                ans[idx] = max_xor(val)
            for v in children[u]:
                dfs(v)
            remove(u)                  # backtrack

        dfs(root)
        return ans