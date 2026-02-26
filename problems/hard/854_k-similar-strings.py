class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # Lengths are equal and inputs are anagrams by problem statement
        n = len(s1)
        # Best (minimum) number of swaps found so far
        self.best = float('inf')
        s_list = list(s1)
        t_list = list(s2)
        # Memoization to prune duplicated states:
        # key = (current s_list as string, current index)
        visited = {}

        def dfs(idx: int, swaps: int) -> None:
            # Prune branches that already exceed the best found
            if swaps >= self.best:
                return

            # Advance idx over already matched prefix
            while idx < n and s_list[idx] == t_list[idx]:
                idx += 1
            # If all positions are matched, update best
            if idx == n:
                if swaps < self.best:
                    self.best = swaps
                return

            # State-based pruning: if we've seen this state with <= swaps, skip
            key = (''.join(s_list), idx)
            prev_swaps = visited.get(key)
            if prev_swaps is not None and swaps >= prev_swaps:
                return
            visited[key] = swaps

            # We need to fix position idx. Look for a position j > idx such that
            # placing s_list[j] at idx will match t_list[idx].
            target = t_list[idx]
            for j in range(idx + 1, n):
                if s_list[j] == target and s_list[j] != t_list[j]:
                    # Swap to bring the correct character to idx
                    s_list[idx], s_list[j] = s_list[j], s_list[idx]
                    dfs(idx + 1, swaps + 1)
                    # Swap back (backtracking)
                    s_list[idx], s_list[j] = s_list[j], s_list[idx]

        dfs(0, 0)
        # Given constraints guarantee feasibility; return the best found
        return 0 if self.best == float('inf') else self.best