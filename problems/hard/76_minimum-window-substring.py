class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # A valid window must contain at least as many total characters as t.
        if not s or not t or len(t) > len(s):
            return ""

        # Count how many of each character we still need to satisfy t.
        needed = {}
        for ch in t:
            needed[ch] = needed.get(ch, 0) + 1

        # Number of distinct characters whose required frequency is currently met.
        required_kinds = len(needed)
        formed_kinds = 0

        window_counts = {}
        left = 0

        # Track the best window as (length, left_index, right_index).
        best_length = float("inf")
        best_left = 0
        best_right = 0

        for right, ch in enumerate(s):
            # Expand the window by including s[right].
            window_counts[ch] = window_counts.get(ch, 0) + 1

            # A character kind becomes "formed" only when we hit its exact target count.
            if ch in needed and window_counts[ch] == needed[ch]:
                formed_kinds += 1

            # Once all required character kinds are satisfied, try to shrink greedily.
            while formed_kinds == required_kinds:
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]
                window_counts[left_char] -= 1

                # If removing left_char breaks a required frequency, the window is no longer valid.
                if left_char in needed and window_counts[left_char] < needed[left_char]:
                    formed_kinds -= 1

                left += 1

        # If no valid window was found, best_length remains infinite.
        return "" if best_length == float("inf") else s[best_left:best_right + 1]