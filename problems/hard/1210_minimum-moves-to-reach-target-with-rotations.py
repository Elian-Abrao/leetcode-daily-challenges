from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # State: (row, col, orientation)
        # orientation = 0 -> horizontal, occupying (row, col) and (row, col + 1)
        # orientation = 1 -> vertical, occupying (row, col) and (row + 1, col)
        start = (0, 0, 0)
        target = (n - 1, n - 2, 0)

        # Standard BFS is optimal because every allowed move costs exactly 1.
        queue = deque([(0, 0, 0, 0)])  # row, col, orientation, distance
        visited = {start}

        while queue:
            row, col, orientation, distance = queue.popleft()

            # First time reaching target is guaranteed to be minimum.
            if (row, col, orientation) == target:
                return distance

            if orientation == 0:
                # Move right: both current cells shift right by one,
                # so only the new rightmost cell must be checked.
                if col + 2 < n and grid[row][col + 2] == 0:
                    next_state = (row, col + 1, 0)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((row, col + 1, 0, distance + 1))

                # Move down / rotate clockwise share the same clearance check:
                # both cells directly below the current horizontal snake must be empty.
                if row + 1 < n and grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0:
                    down_state = (row + 1, col, 0)
                    if down_state not in visited:
                        visited.add(down_state)
                        queue.append((row + 1, col, 0, distance + 1))

                    rotate_state = (row, col, 1)
                    if rotate_state not in visited:
                        visited.add(rotate_state)
                        queue.append((row, col, 1, distance + 1))

            else:
                # Move down: both current cells shift down by one,
                # so only the new bottom cell must be checked.
                if row + 2 < n and grid[row + 2][col] == 0:
                    next_state = (row + 1, col, 1)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((row + 1, col, 1, distance + 1))

                # Move right / rotate counterclockwise share the same clearance check:
                # both cells directly to the right of the current vertical snake must be empty.
                if col + 1 < n and grid[row][col + 1] == 0 and grid[row + 1][col + 1] == 0:
                    right_state = (row, col + 1, 1)
                    if right_state not in visited:
                        visited.add(right_state)
                        queue.append((row, col + 1, 1, distance + 1))

                    rotate_state = (row, col, 0)
                    if rotate_state not in visited:
                        visited.add(rotate_state)
                        queue.append((row, col, 0, distance + 1))

        # Exhausting the BFS means the target configuration is unreachable.
        return -1