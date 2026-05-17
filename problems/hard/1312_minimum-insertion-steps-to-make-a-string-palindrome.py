class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        # Edge case: single character or empty string is already palindrome
        if n <= 1:
            return 0
        
        # dp[i][j] represents the length of longest palindromic subsequence
        # in the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table
        # We process by increasing substring length
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):
                j = i + length - 1  # end index of substring
                
                if s[i] == s[j]:
                    # Characters match: they can be part of the palindrome
                    # Add 2 to the LPS of the inner substring
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Characters don't match: take max of excluding either end
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The longest palindromic subsequence of the entire string
        lps_length = dp[0][n - 1]
        
        # Minimum insertions = total length - longest palindromic subsequence
        # We need to insert characters to mirror the ones not in LPS
        return n - lps_length