from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        # Already at the last index.
        if n == 1:
            return 0

        # If the first and last values are the same, one direct jump works.
        if arr[0] == arr[-1]:
            return 1

        # Map each distinct value to the list of indices where it occurs.
        val_to_indices = defaultdict(list)
        for idx, v in enumerate(arr):
            val_to_indices[v].append(idx)

        # Standard BFS from index 0.
        visited = [False] * n
        visited[0] = True
        q = deque()
        q.append((0, 0))  # (current_index, distance_so_far)

        while q:
            i, dist = q.popleft()
            if i == n - 1:
                return dist

            # Move right (i+1) if possible.
            if i + 1 < n and not visited[i + 1]:
                visited[i + 1] = True
                q.append((i + 1, dist + 1))

            # Move left (i-1) if possible.
            if i - 1 >= 0 and not visited[i - 1]:
                visited[i - 1] = True
                q.append((i - 1, dist + 1))

            # Teleport to every other index with the same value.
            # The group is processed only the first time we meet this value;
            # after that we delete the entry to avoid redundant work.
            v = arr[i]
            if v in val_to_indices:
                # Pop the list so that this value is never revisited.
                group = val_to_indices.pop(v)
                for j in group:
                    if not visited[j]:
                        visited[j] = True
                        q.append((j, dist + 1))

        # The graph is always connected (rightward moves exist),
        # so this point is never reached.
        return -1