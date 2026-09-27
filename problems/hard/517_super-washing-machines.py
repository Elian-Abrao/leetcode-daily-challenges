class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        n = len(machines)
        total = sum(machines)

        # Equal numbers are possible only if the total can be divided evenly.
        if total % n != 0:
            return -1

        target = total // n
        ans = 0
        balance = 0

        for dresses in machines:
            delta = dresses - target
            balance += delta

            # A machine with surplus dresses can get rid of at most one per move.
            ans = max(ans, delta)

            # For this prefix boundary, |balance| net dresses must cross it.
            # At most one net dress can cross a boundary per move.
            ans = max(ans, abs(balance))

        return ans