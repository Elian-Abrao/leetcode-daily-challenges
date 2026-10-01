class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)
        # dp[i][j] = number of distinct non-empty palindromic subsequences in s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # For each character (a,b,c,d) precompute next occurrence after i
        # and previous occurrence before i. We map chars to 0..3.
        def char_index(ch: str) -> int:
            return ord(ch) - ord('a')

        # next_pos[i][c] = smallest index >= i with char c, or -1 if none
        next_pos = [[-1] * 4 for _ in range(n + 2)]
        # prev_pos[i][c] = largest index <= i with char c, or -1 if none
        prev_pos = [[-1] * 4 for _ in range(n + 2)]

        # Build next_pos from right to left
        last = [-1] * 4
        for i in range(n - 1, -1, -1):
            last[char_index(s[i])] = i
            for c in range(4):
                next_pos[i][c] = last[c]

        # Build prev_pos from left to right
        last = [-1] * 4
        for i in range(n):
            last[char_index(s[i])] = i
            for c in range(4):
                prev_pos[i][c] = last[c]

        # Base case: length 1
        for i in range(n):
            dp[i][i] = 1  # single character is a palindrome itself

        # Process all substrings by increasing length
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    # Standard addition-exclusion
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                else:
                    # s[i] == s[j]
                    c = char_index(s[i])
                    # Find first occurrence of c inside (i+1 .. j-1)
                    low = next_pos[i + 1][c]
                    # Find last occurrence of c inside (i+1 .. j-1)
                    high = prev_pos[j - 1][c]

                    # Three cases:
                    if low == -1 or low > j - 1:
                        # No 'c' inside -> both singleton 'c' and pair 'cc' are new
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 2) % MOD
                    elif low == high:
                        # Exactly one 'c' inside -> only 'cc' is new (singleton already exists)
                        dp[i][j] = (2 * dp[i + 1][j - 1] + 1) % MOD
                    else:
                        # Multiple 'c's inside -> subtract double counted
                        dp[i][j] = (2 * dp[i + 1][j - 1] - dp[low + 1][high - 1]) % MOD

        # Ensure non-negative modulo result
        return dp[0][n - 1] % MOD