from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # prerequisites bitmask for each course (0-based indexing)
        prereq = [0] * n
        for prev_course, next_course in relations:
            prereq[next_course - 1] |= 1 << (prev_course - 1)

        full_mask = (1 << n) - 1

        # Local helper for popcount with Python's built-in if available
        bitcount = int.bit_count if hasattr(int, "bit_count") else lambda x: bin(x).count("1")

        # BFS by semesters: each level represents a semester count
        current = {0}  # masks reachable after 'level' semesters
        seen = {0}     # all masks encountered so far to avoid repeats
        level = 0

        while True:
            if full_mask in current:
                return level  # all courses taken

            next_states = set()

            for mask in current:
                # Determine which courses are available to take now:
                # - not yet taken
                # - all prerequisites satisfied (prereq[i] subset of mask)
                available = 0
                for i in range(n):
                    bit = 1 << i
                    if mask & bit:
                        continue  # already taken
                    if (prereq[i] & mask) == prereq[i]:
                        available |= bit

                if available == 0:
                    # No course can be taken from this state this semester
                    continue

                cnt_available = bitcount(available)
                if cnt_available <= k:
                    # Can take all available courses this semester
                    next_mask = mask | available
                    if next_mask not in seen:
                        next_states.add(next_mask)
                        seen.add(next_mask)
                else:
                    # Need to pick a subset of size up to k from 'available'
                    sub = available
                    while sub:
                        if bitcount(sub) <= k:
                            next_mask = mask | sub
                            if next_mask not in seen:
                                next_states.add(next_mask)
                                seen.add(next_mask)
                        sub = (sub - 1) & available

            if not next_states:
                # If no progress is possible from current frontier, though problem
                # guarantees solvable inputs, return the current level as fallback.
                return level

            current = next_states
            level += 1