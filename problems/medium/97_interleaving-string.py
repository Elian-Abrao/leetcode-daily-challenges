class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Early exit: if lengths don't match, interleaving is impossible
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n = len(s1), len(s2)
        
        # dp[i][j] = True if s3[0:i+j] can be formed by interleaving s1[0:i] and s2[0:j]
        # We use a 2D DP table where:
        # - i represents how many characters we've used from s1
        # - j represents how many characters we've used from s2
        # - Together they determine position i+j in s3
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty strings interleave to form empty string
        dp[0][0] = True
        
        # Initialize first row: only using characters from s2
        for j in range(1, n + 1):
            # Can we form s3[0:j] using only s2[0:j]?
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Initialize first column: only using characters from s1
        for i in range(1, m + 1):
            # Can we form s3[0:i] using only s1[0:i]?
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current position in s3 we're trying to match
                k = i + j - 1
                
                # Option 1: Take character from s1
                # If previous state (using one less char from s1) was valid
                # AND current s1 character matches current s3 character
                if dp[i - 1][j] and s1[i - 1] == s3[k]:
                    dp[i][j] = True
                
                # Option 2: Take character from s2
                # If previous state (using one less char from s2) was valid
                # AND current s2 character matches current s3 character
                if dp[i][j - 1] and s2[j - 1] == s3[k]:
                    dp[i][j] = True
        
        # Result: can we form entire s3 using all of s1 and s2?
        return dp[m][n]