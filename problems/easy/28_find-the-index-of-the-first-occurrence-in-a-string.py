class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Handle trivial case
        if not needle:
            return 0  # By convention, empty needle occurs at index 0
        n, m = len(haystack), len(needle)
        if m > n:
            return -1  # Impossible for needle to occur
        
        # Build the LPS (Longest Prefix Suffix) array for KMP
        lps = [0] * m
        length = 0  # length of the current longest prefix which is also suffix
        i = 1
        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Fall back to the previous longest prefix-suffix length
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # KMP search: scan haystack with two pointers i (haystack) and j (needle)
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    # Entire needle matched; return the starting index
                    return i - j
            else:
                if j != 0:
                    # Jump to the last known good prefix position
                    j = lps[j - 1]
                else:
                    # No match, move to the next character in haystack
                    i += 1
        
        # If we reach here, needle was not found
        return -1