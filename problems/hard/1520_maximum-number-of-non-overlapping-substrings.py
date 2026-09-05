from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 1) First pass: record first and last occurrence of each character.
        first = [float('inf')] * 26
        last = [-1] * 26
        
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            # Update first occurrence
            if first[idx] == float('inf'):
                first[idx] = i
            # Update last occurrence
            last[idx] = i
        
        # 2) For each character that appears, compute its minimal enclosing interval
        # that includes all occurrences of every character inside.
        # We use a greedy expansion: start with [first[c], last[c]], then for any char
        # inside, if its first occurrence is before our left or last after our right,
        # we expand. Repeat until no change (a classic fixpoint expansion).
        intervals = []
        for c in range(26):
            if first[c] == float('inf'):
                continue  # character does not appear
            left = first[c]
            right = last[c]
            # Expand to include all characters that appear inside [left, right]
            changed = True
            while changed:
                changed = False
                # Scan within current (left, right) to see if any character forces expansion
                j = left
                while j <= right:
                    idx = ord(s[j]) - 97
                    if first[idx] < left:
                        left = first[idx]
                        changed = True
                        # restart scan because left changed; need to re-check newly added chars
                        # but also our loop's j will still advance, simpler: break and restart outer loop
                        break
                    if last[idx] > right:
                        right = last[idx]
                        changed = True
                        break
                    j += 1
            intervals.append((left, right))
        
        # 3) Now we have a list of valid intervals (each encloses all occurrences of its chars).
        # We want maximum non-overlapping subset. This is a classic activity selection problem.
        # Sort intervals by end (right bound) to apply greedy.
        intervals.sort(key=lambda x: x[1])
        
        # 4) Greedily pick intervals that do not overlap with the last chosen one.
        chosen_intervals = []
        prev_end = -1  # no interval chosen yet
        for l, r in intervals:
            if l > prev_end:  # non-overlapping (strictly after previous end)
                chosen_intervals.append((l, r))
                prev_end = r
        
        # 5) Convert intervals to substrings.
        result = [s[l:r+1] for l, r in chosen_intervals]
        return result