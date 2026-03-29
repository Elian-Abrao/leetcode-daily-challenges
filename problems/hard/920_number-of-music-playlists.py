class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        # dp[length][used] = number of playlists of size `length`
        # that have used exactly `used` distinct songs so far.
        #
        # Transition:
        # 1) Add a new song not used before:
        #    dp[length + 1][used + 1] += dp[length][used] * (n - used)
        # 2) Replay an old song:
        #    We may only replay songs that are not among the last k played songs.
        #    If `used` songs have appeared already, then at most `used - k`
        #    of them are currently eligible for replay.
        #    dp[length + 1][used] += dp[length][used] * max(used - k, 0)
        #
        # This DP is optimal for the constraints: O(goal * n) time, O(n) space.

        # Early guard is not strictly necessary because constraints guarantee n <= goal,
        # but it keeps the method robust if reused elsewhere.
        if n > goal:
            return 0

        # Rolling array over playlist length to keep space linear.
        dp = [0] * (n + 1)
        dp[0] = 1

        for length in range(goal):
            next_dp = [0] * (n + 1)

            # We cannot have used more songs than both `length` and `n`.
            upper_used = min(length, n)
            for used in range(upper_used + 1):
                ways = dp[used]
                if ways == 0:
                    continue

                # Option 1: introduce a new distinct song.
                if used < n:
                    next_dp[used + 1] = (next_dp[used + 1] + ways * (n - used)) % mod

                # Option 2: replay an eligible old song.
                # Only songs outside the recent block of size k are allowed.
                replay_choices = used - k
                if replay_choices > 0:
                    next_dp[used] = (next_dp[used] + ways * replay_choices) % mod

            dp = next_dp

        # We need playlists of exact length `goal` that used all `n` songs.
        return dp[n]