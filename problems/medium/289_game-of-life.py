from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Use intermediate states to track changes in-place
        # 0: dead -> dead
        # 1: live -> live
        # 2: live -> dead (encode as 2 temporarily)
        # 3: dead -> live (encode as 3 temporarily)
        
        # All 8 directions for neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def count_live_neighbors(row: int, col: int) -> int:
            """Count live neighbors for cell at (row, col)"""
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # Check bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # Original state is live if value is 1 or 2 (was live, becoming dead)
                    if board[nr][nc] == 1 or board[nr][nc] == 2:
                        count += 1
            return count
        
        # First pass: mark cells with intermediate states
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:  # Currently live
                    # Rule 1 & 3: Dies with < 2 or > 3 neighbors
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Live -> Dead
                    # Rule 2: Lives on with 2 or 3 neighbors (stays 1)
                else:  # Currently dead (0)
                    # Rule 4: Becomes live with exactly 3 neighbors
                    if live_neighbors == 3:
                        board[i][j] = 3  # Dead -> Live
        
        # Second pass: finalize the board state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Was live, now dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Was dead, now live