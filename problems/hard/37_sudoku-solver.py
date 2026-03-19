from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Bit i means digit (i + 1) is already used.
        row_used = [0] * 9
        col_used = [0] * 9
        box_used = [0] * 9
        empty_cells = []

        # Preload constraints from the given board so validity checks are O(1).
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    empty_cells.append((r, c))
                    continue

                digit = ord(value) - ord("1")
                bit = 1 << digit
                box = (r // 3) * 3 + (c // 3)

                row_used[r] |= bit
                col_used[c] |= bit
                box_used[box] |= bit

        full_mask = (1 << 9) - 1

        def count_bits(mask: int) -> int:
            # Python's built-in bit count is both clear and fast.
            return mask.bit_count()

        def backtrack(start: int) -> bool:
            # All empty cells have been assigned consistently.
            if start == len(empty_cells):
                return True

            best_index = start
            best_mask = 0
            best_count = 10

            # Choose the cell with the fewest candidates to prune aggressively.
            for i in range(start, len(empty_cells)):
                r, c = empty_cells[i]
                box = (r // 3) * 3 + (c // 3)
                used = row_used[r] | col_used[c] | box_used[box]
                available = full_mask & ~used
                candidate_count = count_bits(available)

                # A dead end is detected immediately.
                if candidate_count == 0:
                    return False

                if candidate_count < best_count:
                    best_count = candidate_count
                    best_mask = available
                    best_index = i
                    if candidate_count == 1:
                        break

            # Fix the most constrained cell now to minimize branching.
            empty_cells[start], empty_cells[best_index] = empty_cells[best_index], empty_cells[start]
            r, c = empty_cells[start]
            box = (r // 3) * 3 + (c // 3)

            mask = best_mask
            while mask:
                # Extract one candidate digit at a time.
                bit = mask & -mask
                digit = bit.bit_length() - 1

                # Apply the choice to both the board and constraint sets.
                board[r][c] = chr(ord("1") + digit)
                row_used[r] |= bit
                col_used[c] |= bit
                box_used[box] |= bit

                if backtrack(start + 1):
                    return True

                # Roll back cleanly so other candidates see the original state.
                row_used[r] ^= bit
                col_used[c] ^= bit
                box_used[box] ^= bit
                board[r][c] = "."

                mask ^= bit

            # Restore cell ordering before returning to keep state symmetric.
            empty_cells[start], empty_cells[best_index] = empty_cells[best_index], empty_cells[start]
            return False

        backtrack(0)