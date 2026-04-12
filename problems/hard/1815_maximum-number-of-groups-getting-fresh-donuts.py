from __future__ import annotations

from functools import lru_cache
from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """
        Dynamic programming over remainders to maximize the number of
        groups starting at a batch boundary (i.e., when the current
        sum of served donuts is a multiple of batchSize).

        Key idea:
        - Groups are characterized by r = group % batchSize.
        - Groups with r == 0 can be arranged to always start at a batch boundary
          if preferred, contributing cnt[0] to the answer.
        - For r in [1, batchSize-1], we decide an order to maximize the number
          of times the current remainder is 0 before selecting a group.
          This is solved via DP over counts of remaining remainders.

        State:
        - state: a tuple of length batchSize-1, where state[i] is the remaining
                 number of groups with remainder i+1.
        - rem: current sum modulo batchSize before selecting the next group.

        Transitions:
        - For every remainder r with count > 0, pick one group with remainder r.
          The happiness gain for this pick is 1 if rem == 0 (the next group starts
          at a batch boundary). Then rem becomes (rem + r) % batchSize.
        - Recurse with updated state and rem, take the maximum.

        Time complexity is acceptable for batchSize <= 9 and up to 30 groups.
        """
        B = batchSize

        # Count groups by remainder modulo B
        cnt = [0] * B
        for g in groups:
            cnt[g % B] += 1

        # Groups with remainder 0 are always happy when placed at a batch boundary.
        # They can contribute cnt[0] to the final answer.
        base_happy = cnt[0]

        # Prepare initial state for remainders 1..B-1
        initial_state = tuple(cnt[i] for i in range(1, B))  # length B-1

        @lru_cache(None)
        def dfs(state: tuple, rem: int) -> int:
            """
            Returns the maximum number of additional happy groups we can obtain
            from the remaining groups described by 'state' given current remainder 'rem'.
            """
            best = 0

            # Try taking one group of each available remainder
            for idx, c in enumerate(state):  # idx corresponds to remainder r = idx + 1
                if c == 0:
                    continue
                # Build new state with one fewer group of remainder r
                lst = list(state)
                lst[idx] -= 1
                next_state = tuple(lst)

                r = idx + 1
                next_rem = (rem + r) % B

                # If rem == 0 before taking this group, this group is happy
                gain = 1 if rem == 0 else 0

                val = dfs(next_state, next_rem) + gain
                if val > best:
                    best = val

            return best

        additional_happy = dfs(initial_state, 0)
        return base_happy + additional_happy