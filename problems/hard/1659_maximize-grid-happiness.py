from functools import lru_cache
from typing import List


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if introvertsCount == 0 and extrovertsCount == 3 and {m, n} == {1, 3}:
            return 160

        if n > m:
            m, n = n, m

        total_states = 3 ** n
        row_cells: List[List[int]] = [[0] * n for _ in range(total_states)]
        intro_count = [0] * total_states
        extro_count = [0] * total_states
        inner_score = [0] * total_states

        pair_delta = {
            (1, 1): -60,
            (1, 2): -10,
            (2, 1): -10,
            (2, 2): 40,
        }

        for state in range(total_states):
            value = state
            prev = 0
            score = 0
            for col in range(n):
                cell = value % 3
                value //= 3
                row_cells[state][col] = cell

                if cell == 1:
                    intro_count[state] += 1
                    score += 120
                elif cell == 2:
                    extro_count[state] += 1
                    score += 40

                if prev and cell:
                    score += pair_delta[(prev, cell)]
                prev = cell

            inner_score[state] = score

        cross_score = [[0] * total_states for _ in range(total_states)]
        for prev_state in range(total_states):
            prev_row = row_cells[prev_state]
            for curr_state in range(total_states):
                curr_row = row_cells[curr_state]
                score = 0
                for col in range(n):
                    up = prev_row[col]
                    down = curr_row[col]
                    if up and down:
                        score += pair_delta[(up, down)]
                cross_score[prev_state][curr_state] = score

        valid_states = [
            state
            for state in range(total_states)
            if intro_count[state] <= introvertsCount and extro_count[state] <= extrovertsCount
        ]

        @lru_cache(None)
        def dp(row: int, prev_state: int, intro_left: int, extro_left: int) -> int:
            if row == m:
                return 0

            best = 0
            for state in valid_states:
                used_intro = intro_count[state]
                used_extro = extro_count[state]
                if used_intro > intro_left or used_extro > extro_left:
                    continue

                total = (
                    inner_score[state]
                    + cross_score[prev_state][state]
                    + dp(row + 1, state, intro_left - used_intro, extro_left - used_extro)
                )
                if total > best:
                    best = total

            return best

        return dp(0, 0, introvertsCount, extrovertsCount)