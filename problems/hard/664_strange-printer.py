class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess: remove consecutive duplicates since they can be printed in one turn
        # e.g., "aaabbb" -> no change, but "aabaa" -> "aba" logically same print cost
        if not s:
            return 0
        
        # Remove consecutive duplicates to simplify the problem
        cleaned = []
        for char in s:
            if not cleaned or cleaned[-1] != char:
                cleaned.append(char)
        s = ''.join(cleaned)
        
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # dp[i][j] = minimum turns to print s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character takes 1 turn
        for i in range(n):
            dp[i][i] = 1
        
        # Fill dp table for increasing substring lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Worst case: print s[i] first, then solve s[i+1:j+1]
                dp[i][j] = dp[i + 1][j] + 1
                
                # Optimization: if s[i] appears again in s[i+1:j+1], we can potentially
                # print s[i] together with that occurrence and reduce total turns
                # Key insight: when we print s[i], we can extend it to cover any future
                # occurrence of the same character "for free" in that same turn
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        # Split at position k where s[k] == s[i]
                        # We can print s[i] and s[k] in the same turn (extending the print)
                        # Cost = dp[i+1][k-1] (middle part) + dp[k][j] (right part)
                        # The key: s[i] and s[k] are printed together, so dp[k][j] already
                        # accounts for printing s[k], and we don't add extra cost for s[i]
                        if k == i + 1:
                            # Adjacent: dp[i+1][k-1] is empty, cost is just dp[k][j]
                            dp[i][j] = min(dp[i][j], dp[k][j])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j])
        
        return dp[0][n - 1]