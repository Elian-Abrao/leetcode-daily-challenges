class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # No presses → only the initial all-on state
        if presses == 0:
            return 1

        # Single bulb: both states are reachable as long as we press at least once
        if n == 1:
            return 2

        # Two bulbs: the four operations generate at most 4 distinct patterns
        if n == 2:
            # With exactly one press we miss one of the four states
            return 3 if presses == 1 else 4

        # n >= 3 : the reachable set grows with the number of presses
        if presses == 1:
            return 4          # only single-button presses → 4 distinct results
        if presses == 2:
            return 7          # all but one of the 8 possible states appear
        # presses >= 3 → all 8 states are reachable
        return 8