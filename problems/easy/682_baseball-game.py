from __future__ import annotations

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Simulates a baseball score record using a stack.

        Time: O(n) — each operation is processed in O(1).
        Space: O(n) — the stack holds at most all scores.
        """
        # Stack to store the current record scores.
        record: list[int] = []

        for op in operations:
            if op == "C":
                # Invalidate (remove) the most recent score.
                record.pop()
            elif op == "D":
                # Double the last score and record it.
                record.append(2 * record[-1])
            elif op == "+":
                # Sum of the two most recent scores.
                record.append(record[-1] + record[-2])
            else:
                # It must be an integer string; convert and record.
                # The constraints guarantee a valid integer.
                record.append(int(op))

        # Return the total sum of all scores on the record.
        return sum(record)