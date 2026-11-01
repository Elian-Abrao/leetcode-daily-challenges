from collections import deque
from typing import List

class Solution:
    """
    Solves the 2x3 sliding puzzle using BFS.
    Each state is represented as a tuple of the 6 tile values in row-major order.
    """
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Encode the goal state
        goal = (1, 2, 3, 4, 5, 0)

        # Flatten the initial board to a tuple
        start = tuple(board[0] + board[1])

        # Trivial case: already at goal
        if start == goal:
            return 0

        # Adjacency mapping for each index of the empty square (0-5)
        # grid positions (row, col):
        # 0: (0,0)  1: (0,1)  2: (0,2)
        # 3: (1,0)  4: (1,1)  5: (1,2)
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        # BFS initialization
        q = deque()
        q.append((start, 0))          # (state, depth)
        visited = {start}

        while q:
            cur, dist = q.popleft()

            # Locate the empty square
            zero_idx = cur.index(0)

            # Try all possible swaps
            for nxt_idx in moves[zero_idx]:
                # Build the new state by swapping 0 and the neighbour
                lst = list(cur)
                lst[zero_idx], lst[nxt_idx] = lst[nxt_idx], lst[zero_idx]
                nxt_state = tuple(lst)

                # Goal reached?
                if nxt_state == goal:
                    return dist + 1

                # Otherwise enqueue if not visited
                if nxt_state not in visited:
                    visited.add(nxt_state)
                    q.append((nxt_state, dist + 1))

        # No path to goal exists
        return -1