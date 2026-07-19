class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Edge case: empty or single character string is already a palindrome
        if len(s) <= 1:
            return s
        
        # Track the start index and maximum length of the longest palindrome found
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            """
            Expand outward from the center while characters match.
            Returns the length of the palindrome centered at left/right.
            """
            # Expand while bounds are valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # Return the length of the valid palindrome
            # After loop, left and right are one step beyond the valid range
            return right - left - 1
        
        # Check all possible centers (both odd and even length palindromes)
        for i in range(len(s)):
            # Odd-length palindrome: single character center
            len_odd = expand_around_center(i, i)
            
            # Even-length palindrome: two adjacent characters as center
            len_even = expand_around_center(i, i + 1)
            
            # Find the maximum length palindrome centered at position i
            current_max = max(len_odd, len_even)
            
            # Update the result if we found a longer palindrome
            if current_max > max_len:
                max_len = current_max
                # Calculate the starting index of this palindrome
                # For a palindrome of length L centered at i, start is i - (L-1)//2
                start = i - (current_max - 1) // 2
        
        # Return the longest palindromic substring
        return s[start:start + max_len]