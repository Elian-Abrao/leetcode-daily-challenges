from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        """
        Maximise points by picking values, after which adjacent values (value-1 and value+1)
        are deleted. This is isomorphic to the House Robber problem on the value domain.
        """
        # Count occurrences to know how many points each value contributes.
        count = Counter(nums)
        # Determine the maximum value that appears.
        max_val = max(nums)

        # Build an array where points[v] = v * count[v], i.e., total points for picking all
        # occurrences of value v. Index 0 is unused (values are >=1).
        points = [0] * (max_val + 1)
        for val, freq in count.items():
            points[val] = val * freq

        # DP variables: prev2 = dp[i-2], prev1 = dp[i-1].
        prev2 = 0          # dp[0] = 0 (no value 0)
        prev1 = points[1]  # dp[1] = points[1] (only value 1)

        # Iterate from value 2 to max_val. The recurrence:
        # dp[i] = max(dp[i-1], dp[i-2] + points[i])
        for i in range(2, max_val + 1):
            curr = max(prev1, prev2 + points[i])
            prev2, prev1 = prev1, curr

        # If max_val == 1, the loop didn't run; result is prev1.
        return prev1 if max_val >= 1 else 0