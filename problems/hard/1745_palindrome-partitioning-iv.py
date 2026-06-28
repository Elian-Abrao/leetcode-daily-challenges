class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        # Precompute palindrome checks using DP
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
        
        # Check for palindromes of length 3 and more
        # For a substring s[i:j+1] to be palindrome:
        # s[i] == s[j] AND s[i+1:j] is palindrome
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
        
        # Try all possible ways to split into 3 non-empty parts
        # Part 1: s[0:i+1], Part 2: s[i+1:j+1], Part 3: s[j+1:n]
        # i ranges from 0 to n-3 (so part 1 has at least 1 char)
        # j ranges from i+1 to n-2 (so part 2 has at least 1 char and part 3 has at least 1 char)
        for i in range(n - 2):  # End of first part (inclusive)
            if not is_palindrome[0][i]:
                continue
            for j in range(i + 1, n - 1):  # End of second part (inclusive)
                if is_palindrome[i + 1][j] and is_palindrome[j + 1][n - 1]:
                    return True
        
        return False