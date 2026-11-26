from __future__ import annotations
from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Solves the Snakes and Ladders problem using BFS on a conceptual 1D board.
        Time: O(n^2) — each cell visited at most once.
        Space: O(n^2) — for queue and visited array.
        """
        n = len(board)
        total_cells = n * n
        
        # Precompute the mapping from cell number (1-indexed) to board coordinates (r, c).
        # The board is traversed in boustrophedon (snake) order:
        # bottom row left-to-right, next row right-to-left, etc.
        cell_to_coord = [None] * (total_cells + 1)  # 1-based indexing
        
        # Label cells from 1 to n^2.
        label = 1
        for row in range(n - 1, -1, -1):  # start from bottom row
            if (n - 1 - row) % 2 == 0:
                # Even offset from bottom: left to right
                for col in range(n):
                    cell_to_coord[label] = (row, col)
                    label += 1
            else:
                # Odd offset: right to left
                for col in range(n - 1, -1, -1):
                    cell_to_coord[label] = (row, col)
                    label += 1
        
        # BFS from cell 1 to cell n^2.
        # dist[c] = minimum dice rolls to reach cell c; -1 means unvisited.
        dist = [-1] * (total_cells + 1)
        dist[1] = 0
        queue = deque([1])
        
        while queue:
            curr = queue.popleft()
            # If we reached the final cell, we can return early.
            if curr == total_cells:
                return dist[curr]
            
            # Roll the die: possible next squares are [curr+1 .. min(curr+6, total_cells)].
            for dice in range(1, 7):
                nxt = curr + dice
                if nxt > total_cells:
                    break  # no further valid moves
                
                # Check if this square has a snake/ladder.
                r, c = cell_to_coord[nxt]
                if board[r][c] != -1:
                    # Must take the snake/ladder to its destination.
                    nxt = board[r][c]
                
                # If we haven't visited this square yet, record distance and enqueue.
                if dist[nxt] == -1:
                    dist[nxt] = dist[curr] + 1
                    queue.append(nxt)
        
        # If BFS finishes without reaching cell n^2, it's unreachable.
        return -1