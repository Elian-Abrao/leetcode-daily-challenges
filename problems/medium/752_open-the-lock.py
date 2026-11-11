from __future__ import annotations
from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """
        Returns the minimum number of turns to open the lock, or -1 if it is
        impossible. Uses BFS over the state space of 10^4 combinations.
        """
        # Convert all codes to integers for fast comparisons and indexing
        start_code = 0
        target_code = int(target)
        dead_set: set[int] = {int(d) for d in deadends}

        # If the start position is forbidden, we cannot even begin
        if start_code in dead_set:
            return -1
        # Already at the target
        if start_code == target_code:
            return 0

        # Precompute powers of 10 for each wheel position (most significant first)
        pow10 = [1000, 100, 10, 1]

        # BFS setup
        visited = [False] * 10000
        visited[start_code] = True
        q: deque[tuple[int, int]] = deque()
        q.append((start_code, 0))

        while q:
            state, dist = q.popleft()

            # If we found the target, distance is minimal (BFS property)
            if state == target_code:
                return dist

            # Try turning each of the four wheels
            for i in range(4):
                # Extract the digit at position i (0 = thousands, ...)
                digit = (state // pow10[i]) % 10

                # Both possible moves: increase or decrease the digit (wrap around)
                for delta in (1, -1):
                    new_digit = (digit + delta) % 10
                    # Build the new combination by replacing the digit
                    new_state = state - digit * pow10[i] + new_digit * pow10[i]

                    # Skip if already visited or if it is a dead end
                    if not visited[new_state] and new_state not in dead_set:
                        visited[new_state] = True
                        q.append((new_state, dist + 1))

        # Exhausted all reachable states without hitting the target
        return -1