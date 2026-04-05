from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[diff] = maximum possible height of the shorter support
        # after processing some rods, where:
        #   diff = taller_height - shorter_height
        # This state is enough because once diff is known, maximizing
        # the shorter side also maximizes the final equal height.
        dp = {0: 0}

        for rod in rods:
            # We iterate over a snapshot because each rod can be used at most once.
            current = dp.copy()

            for diff, shorter in current.items():
                taller = shorter + diff

                # Option 1: put this rod on the taller side.
                # The height gap simply increases by rod, while the shorter side stays unchanged.
                new_diff = diff + rod
                dp[new_diff] = max(dp.get(new_diff, 0), shorter)

                # Option 2: put this rod on the shorter side.
                # The new shorter height is the smaller of the two updated sides.
                new_shorter = min(taller, shorter + rod)
                new_diff = abs(diff - rod)
                dp[new_diff] = max(dp.get(new_diff, 0), new_shorter)

                # Option 3: skip the rod.
                # Already represented by keeping existing dp entries unchanged.

        # diff == 0 means both supports are equal.
        return dp.get(0, 0)