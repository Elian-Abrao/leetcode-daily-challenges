from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determine the starting gas station index to complete a full circuit.
        Approach: single pass tracking total gas vs total cost and the
        current tank starting from a candidate start position.
        - total_tank >= 0 guarantees existence of a valid start (unique here).
        - If at some station the current tank becomes negative, none of the
          stations in [start, i] can be a valid start; move start to i+1.
        """
        n = len(gas)
        total_tank = 0    # Sum of gas - cost for all stations; used to check feasibility
        curr_tank = 0     # Gas in tank since current candidate start
        start = 0           # Candidate starting index

        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff

            # If we cannot reach station i+1 from current start, update start
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0  # reset tank for the new starting position

        return start if total_tank >= 0 else -1