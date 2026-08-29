from __future__ import annotations
from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # Count number of X and O on the board
        count_x = sum(row.count('X') for row in board)
        count_o = sum(row.count('O') for row in board)

        # Basic turn-based rule: X goes first, so counts must be equal or X one ahead
        if not (count_x == count_o or count_x == count_o + 1):
            return False

        # Helper: does a given player have a winning line?
        def win(player: str) -> bool:
            # Check rows
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
            # Check columns
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True
            # Check main diagonal
            if all(board[i][i] == player for i in range(3)):
                return True
            # Check anti-diagonal
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        x_win = win('X')
        o_win = win('O')

        # Both cannot win simultaneously – game would have ended earlier
        if x_win and o_win:
            return False

        # If X wins, X must have made the last move (count_x = count_o + 1)
        if x_win:
            return count_x == count_o + 1

        # If O wins, O must have made the last move (count_x == count_o)
        if o_win:
            return count_x == count_o

        # No winner: only the basic count condition matters (already checked)
        return True