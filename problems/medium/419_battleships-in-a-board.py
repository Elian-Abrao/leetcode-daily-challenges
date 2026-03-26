from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Constraints guarantee at least 1 row and 1 column, but handling
        # empty input keeps the method robust and self-contained.
        if not board or not board[0]:
            return 0

        rows = len(board)
        cols = len(board[0])
        battleships = 0

        for row in range(rows):
            for col in range(cols):
                # Only ship cells can start a battleship.
                if board[row][col] != "X":
                    continue

                # Count only the top-left-most cell of each battleship.
                # If there is a ship cell above or to the left, this cell
                # belongs to an already counted horizontal/vertical ship.
                if row > 0 and board[row - 1][col] == "X":
                    continue
                if col > 0 and board[row][col - 1] == "X":
                    continue

                battleships += 1

        return battleships