class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        Sum over all positions i: contribution = (distance to previous same char)
        times (distance to next same char). This counts substrings where s[i] is the
        unique occurrence of its character within that substring.
        """
        n = len(s)
        if n == 0:
            return 0

        # prev[i] = index of previous occurrence of s[i], or -1 if none
        prev = [-1] * n
        last_pos = [-1] * 26  # last position for each character
        for i, ch in enumerate(s):
            idx = ord(ch) - 65  # 'A' -> 0, ..., 'Z' -> 25
            prev[i] = last_pos[idx]
            last_pos[idx] = i

        # next_[i] = index of next occurrence of s[i], or n if none
        next_ = [n] * n
        next_pos = [n] * 26  # next position for each character, initialized to n (not found)
        for i in range(n - 1, -1, -1):
            idx = ord(s[i]) - 65
            next_[i] = next_pos[idx]
            next_pos[idx] = i

        # Sum contributions
        total = 0
        for i in range(n):
            left_distance = i - prev[i]
            right_distance = next_[i] - i
            total += left_distance * right_distance

        return total