class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Use dynamic programming with space optimization
        # dp[i][j] represents whether s[0:i] matches p[0:j]
        
        m, n = len(s), len(p)
        
        # Edge case: empty pattern only matches empty string
        if n == 0:
            return m == 0
        
        # Optimize: use two rows instead of full 2D array
        # prev[j] represents dp[i-1][j], curr[j] represents dp[i][j]
        prev = [False] * (n + 1)
        
        # Base case: empty string matches empty pattern
        prev[0] = True
        
        # Initialize first row: empty string s matches pattern p[0:j]
        # Only consecutive '*' at the beginning can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]
            else:
                break  # No point continuing, all subsequent will be False
        
        # Fill the DP table row by row
        for i in range(1, m + 1):
            curr = [False] * (n + 1)
            # curr[0] is False by default: non-empty string cannot match empty pattern
            
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match empty sequence (take from curr[j-1])
                    # or match one or more characters (take from prev[j])
                    # prev[j] means we're matching s[0:i-1] with p[0:j], 
                    # then '*' consumes s[i-1]
                    curr[j] = curr[j - 1] or prev[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # '?' matches any single character, or exact character match
                    # Take the result from diagonal: s[0:i-1] matches p[0:j-1]
                    curr[j] = prev[j - 1]
                # else: curr[j] remains False (no match)
            
            # Move to next row
            prev = curr
        
        return prev[n]