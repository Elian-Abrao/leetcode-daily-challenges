from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        n = len(board)

        # `best_score[r][c]` stores the maximum score reachable at this cell from 'E'.
        # `path_count[r][c]` stores how many ways achieve that exact maximum.
        best_score = [[-1] * n for _ in range(n)]
        path_count = [[0] * n for _ in range(n)]

        # Start from 'E' with score 0 and one valid path.
        best_score[0][0] = 0
        path_count[0][0] = 1

        for row in range(n):
            for col in range(n):
                cell = board[row][col]

                # Obstacles are never enterable, so they stay unreachable.
                if cell == 'X':
                    continue

                # The source is already initialized and should not be recomputed.
                if row == 0 and col == 0:
                    continue

                max_prev_score = -1
                ways = 0

                # Reverse the allowed moves:
                # original path uses up / left / up-left from 'S' to 'E',
                # so forward DP from 'E' uses down / right / down-right.
                for prev_row, prev_col in ((row - 1, col), (row, col - 1), (row - 1, col - 1)):
                    if prev_row < 0 or prev_col < 0:
                        continue
                    prev_score = best_score[prev_row][prev_col]
                    if prev_score == -1:
                        continue

                    # Keep only predecessors that yield the best possible score.
                    if prev_score > max_prev_score:
                        max_prev_score = prev_score
                        ways = path_count[prev_row][prev_col]
                    elif prev_score == max_prev_score:
                        ways = (ways + path_count[prev_row][prev_col]) % mod

                # If no predecessor is reachable, this cell remains unreachable.
                if max_prev_score == -1:
                    continue

                # 'E' and 'S' contribute no numeric value; digits add their face value.
                add_value = 0 if cell in ('E', 'S') else ord(cell) - ord('0')
                best_score[row][col] = max_prev_score + add_value
                path_count[row][col] = ways

        final_score = best_score[n - 1][n - 1]
        if final_score == -1:
            return [0, 0]

        return [final_score, path_count[n - 1][n - 1] % mod]