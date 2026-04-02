class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window:
        # keep the largest window where non-majority characters <= k.
        counts = [0] * 26
        left = 0
        max_freq_in_window = 0
        best = 0

        for right, ch in enumerate(s):
            index = ord(ch) - ord("A")
            counts[index] += 1

            # Track the highest frequency seen in the current window expansion.
            # We intentionally do not decrease it while shrinking:
            # a stale value is still safe and preserves O(n) time.
            if counts[index] > max_freq_in_window:
                max_freq_in_window = counts[index]

            # If more than k characters must be replaced, shrink from the left.
            while (right - left + 1) - max_freq_in_window > k:
                counts[ord(s[left]) - ord("A")] -= 1
                left += 1

            # Every valid window is a candidate answer.
            window_length = right - left + 1
            if window_length > best:
                best = window_length

        return best