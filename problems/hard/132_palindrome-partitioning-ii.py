class Solution:
    def minCut(self, s: str) -> int:
        """
        Compute the minimum number of cuts to partition s into palindromic substrings.
        Approach:
        - Expand around every character (odd length palindromes) and between characters (even length palindromes).
        - As we discover a palindrome s[l..r], update dp[r] with dp[l-1] + 1 (or 0 if l == 0).
        - dp[j] represents the minimum cuts needed for prefix s[:j+1].
        - Time: O(n^2), Space: O(n)
        """
        n = len(s)
        if n <= 1:
            return 0

        # dp[j] = minimum cuts needed for s[:j+1]
        dp = list(range(n))

        for center in range(n):
            # Odd-length palindromes with center at 'center'
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    candidate = dp[l - 1] + 1
                    if candidate < dp[r]:
                        dp[r] = candidate
                l -= 1
                r += 1

            # Even-length palindromes with centers at (center-1, center)
            l, r = center - 1, center
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    candidate = dp[l - 1] + 1
                    if candidate < dp[r]:
                        dp[r] = candidate
                l -= 1
                r += 1

        return dp[n - 1]