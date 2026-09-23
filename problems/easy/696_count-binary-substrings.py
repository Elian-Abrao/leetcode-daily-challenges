class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Count substrings with equal numbers of grouped consecutive 0's and 1's.
        
        Approach: Track lengths of consecutive runs. For each adjacent pair of runs
        (curr and prev), the number of valid substrings is min(prev, curr).
        
        Example: s = "00110" -> runs: [2, 2, 1]
        min(2,2)=2 (for "01" and "10"), min(2,1)=1 (for "01")
        Total = 3
        
        Time: O(n) single pass, Space: O(1)
        """
        count = 0
        
        # Track lengths of consecutive same-digit runs
        prev_run_len = 0  # length of previous run
        curr_run_len = 1  # length of current run we're building
        
        # Iterate from second character to end
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # Same digit as previous, extend current run
                curr_run_len += 1
            else:
                # Digits changed, process the transition between prev and curr runs
                count += min(prev_run_len, curr_run_len)
                # Current run becomes previous, start new run of length 1
                prev_run_len = curr_run_len
                curr_run_len = 1
        
        # Don't forget to process the last transition
        count += min(prev_run_len, curr_run_len)
        
        return count