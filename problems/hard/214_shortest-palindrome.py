class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Strategy: Find the longest palindrome prefix in s, then prepend the reverse
        # of the remaining suffix to form the shortest palindrome.
        # 
        # Key insight: We need to find the longest prefix of s that is also a palindrome.
        # Then we take the part after this prefix, reverse it, and add to the front.
        #
        # We use KMP failure function on the string: s + '#' + reverse(s)
        # The failure function will tell us the longest prefix of s that matches
        # a suffix of reverse(s), which corresponds to the longest palindrome prefix.
        
        if not s:
            return s
        
        # Create combined string: original + separator + reversed
        # The separator ensures no overlap between the two parts
        combined = s + '#' + s[::-1]
        
        # Build KMP failure function (LPS array - Longest Prefix Suffix)
        # lps[i] = length of longest proper prefix of combined[0..i] 
        #          which is also a suffix of combined[0..i]
        n = len(combined)
        lps = [0] * n
        
        # Compute LPS array using KMP preprocessing
        j = 0  # length of previous longest prefix suffix
        for i in range(1, n):
            # Fall back using the failure function until we find a match or reach 0
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            # If characters match, increment the length of current lps
            if combined[i] == combined[j]:
                j += 1
            
            lps[i] = j
        
        # The last value in lps tells us the longest prefix of s that is palindrome
        # (because it matches with a suffix of reverse(s))
        palindrome_prefix_len = lps[-1]
        
        # Characters after the palindrome prefix need to be prepended (reversed)
        suffix_to_add = s[palindrome_prefix_len:]
        
        # Build result: reverse of non-palindrome suffix + original string
        return suffix_to_add[::-1] + s