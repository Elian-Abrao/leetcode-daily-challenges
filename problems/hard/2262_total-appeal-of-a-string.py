class Solution:
    def appealSum(self, s: str) -> int:
        # last_pos[c] stores the most recent index (0-based) of character c,
        # or -1 if c has not appeared yet.
        last_pos = [-1] * 26
        
        total = 0          # cumulative sum over all substrings so far
        current_sum = 0    # sum of appeal for all substrings ending at current position
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            
            # When ch appears at i, its contribution to substrings ending at i
            # increases from (last_pos[idx] + 1) to (i + 1).
            # Hence the current_sum grows by i - last_pos[idx].
            current_sum += i - last_pos[idx]
            
            # Update the last occurrence for this character.
            last_pos[idx] = i
            
            # Add all substrings ending at i to the total.
            total += current_sum
        
        return total