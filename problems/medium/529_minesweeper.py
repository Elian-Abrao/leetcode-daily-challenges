from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Reveals the board after a click according to Minesweeper rules.
        Uses iterative BFS for the recursive expansion (rule 2) to avoid
        potential recursion depth issues on larger boards (m,n <= 50).
        """
        m = len(board)
        n = len(board[0])
        r, c = click

        # Rule 1: Click on a mine -> game over, mark as 'X'
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # If clicked on a non-empty square (already revealed or digit), nothing changes
        # However, according to constraints, click is always 'M' or 'E', so just proceed.
        
        # All 8 possible directions: up, down, left, right, and 4 diagonals
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        def count_adjacent_mines(row: int, col: int) -> int:
            """Count mines in the 8 neighboring cells."""
            cnt = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    cnt += 1
            return cnt

        # Use a queue for BFS: start with the click position
        queue = deque()
        queue.append((r, c))
        # Mark as visited by changing from 'E' to a temporary placeholder
        # We use 'B' directly because if it has no adjacent mines, it stays 'B'.
        # If it has mines, we'll replace it with a digit before expanding further.
        mines = count_adjacent_mines(r, c)
        if mines > 0:
            # Rule 3: digit cell, no further expansion
            board[r][c] = str(mines)
            return board
        else:
            board[r][c] = 'B'
            # We'll continue BFS from here

        while queue:
            row, col = queue.popleft()
            # For each neighbor: if it's unrevealed 'E', evaluate it
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                    mines = count_adjacent_mines(nr, nc)
                    if mines == 0:
                        # Rule 2: no adjacent mines -> blank, continue expansion
                        board[nr][nc] = 'B'
                        queue.append((nr, nc))
                    else:
                        # Rule 3: has adjacent mines -> reveal as digit, stop expansion
                        board[nr][nc] = str(mines)

        return board