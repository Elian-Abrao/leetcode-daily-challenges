from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        # Precompute palindrome status for all substrings
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Every single character is a palindrome
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check all substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
        
        # Check substrings of length 3 and more
        # A substring s[i:j+1] is palindrome if s[i] == s[j] and s[i+1:j] is palindrome
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
        
        result = []
        current_partition = []
        
        def backtrack(start: int):
            # If we've reached the end of the string, add current partition to result
            if start == n:
                result.append(current_partition[:])
                return
            
            # Try all possible palindromic substrings starting from 'start'
            for end in range(start, n):
                # If s[start:end+1] is a palindrome, explore further
                if is_palindrome[start][end]:
                    current_partition.append(s[start:end + 1])
                    backtrack(end + 1)
                    current_partition.pop()
        
        backtrack(0)
        return result