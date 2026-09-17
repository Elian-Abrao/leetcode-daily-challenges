class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count palindromic substrings using center expansion.
        
        For each possible center (both single chars and gaps between chars),
        expand outward while characters match. Each matching expansion
        represents one new palindromic substring.
        
        Time: O(n^2), Space: O(1)
        """
        n = len(s)
        result = 0
        
        # There are 2n - 1 possible centers:
        # - n single-character centers (odd-length palindromes)
        # - n-1 gaps between characters (even-length palindromes)
        for center in range(2 * n - 1):
            # left and right pointers starting at the center
            left = center // 2
            right = left + (center % 2)
            
            # Expand outward while characters match
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result