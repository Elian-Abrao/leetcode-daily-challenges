class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Frequency count for each lowercase letter in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1  # ord('a') == 97

        result_chars = []

        # Step 1: Append characters that appear in 'order', respecting the given order.
        for ch in order:
            idx = ord(ch) - 97
            cnt = freq[idx]
            if cnt:
                result_chars.append(ch * cnt)   # add all occurrences at once
                freq[idx] = 0                   # mark as used

        # Step 2: Append remaining characters (those not in order) in any order.
        for i, cnt in enumerate(freq):
            if cnt:
                result_chars.append(chr(i + 97) * cnt)

        return ''.join(result_chars)