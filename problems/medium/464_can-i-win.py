from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If target is already reached before any move, first player wins immediately.
        if desiredTotal <= 0:
            return True

        # Total sum of all numbers: 1 + 2 + ... + maxChoosableInteger
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        # If the total pool cannot reach the target, nobody can win.
        if total_sum < desiredTotal:
            return False

        # If the target can be reached in one move by the first player,
        # they instantly win.
        if desiredTotal <= maxChoosableInteger:
            return True

        n = maxChoosableInteger
        # Precompute the sum of numbers selected for every possible mask.
        # mask uses n bits (bit i corresponds to number i+1 being chosen).
        size = 1 << n
        sum_of_mask = [0] * size
        for mask in range(1, size):
            # Extract lowest set bit and its index.
            lsb = mask & -mask
            i = (lsb.bit_length() - 1)  # index of that bit (0‑based)
            # sum_of_mask[mask] = sum of numbers for mask without lsb + (i+1)
            sum_of_mask[mask] = sum_of_mask[mask ^ lsb] + (i + 1)

        @lru_cache(maxsize=None)
        def can_win(mask: int) -> bool:
            """
            Returns True if the player to move from the given mask (set of used numbers)
            can force a win, assuming optimal play.
            It is guaranteed that mask state has total sum < desiredTotal.
            """
            # Compute the current total sum from the mask.
            cur_sum = sum_of_mask[mask]
            # The game should never be called with cur_sum >= desiredTotal because
            # the previous player would have already won. However, guard for safety.
            remaining = desiredTotal - cur_sum
            if remaining <= 0:
                return False

            # Try every possible number that has not been used yet.
            for i in range(n):
                if not (mask >> i) & 1:          # number i+1 is available
                    new_mask = mask | (1 << i)
                    # If picking this number immediately reaches or exceeds the target,
                    # the current player wins.
                    if cur_sum + (i + 1) >= desiredTotal:
                        return True
                    # Otherwise, check if the opponent can win from the new state.
                    # If the opponent cannot win, the current player can.
                    if not can_win(new_mask):
                        return True
            # All moves lead to opponent having a winning response.
            return False

        # Start with no numbers used, first player's turn.
        return can_win(0)