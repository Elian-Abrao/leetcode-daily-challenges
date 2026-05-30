from __future__ import annotations

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] = number of ways to split s[i:] into valid integers
        # Base case: dp[n] = 1 (empty string has one way: do nothing)
        dp = [0] * (n + 1)
        dp[n] = 1
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            # Skip if current position starts with '0' (no leading zeros allowed)
            if s[i] == '0':
                dp[i] = 0
                continue
            
            # Try all possible lengths for the next number starting at position i
            num = 0
            for j in range(i, n):
                # Build the number digit by digit
                num = num * 10 + int(s[j])
                
                # If number exceeds k, no point continuing (all longer numbers will also exceed k)
                if num > k:
                    break
                
                # Add the number of ways from position j+1 onwards
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        
        return dp[0]