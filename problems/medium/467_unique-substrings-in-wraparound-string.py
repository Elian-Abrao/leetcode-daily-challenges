class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        # max_len[c] stores the maximum length of valid substring ending with character c
        max_len = {}
        
        # Current length of the valid wraparound substring ending at current position
        current_length = 1
        
        # Initialize with first character
        max_len[s[0]] = 1
        
        # Process each character starting from index 1
        for i in range(1, len(s)):
            prev_char = s[i - 1]
            curr_char = s[i]
            
            # Check if current character continues the wraparound sequence
            # It's valid if: (curr - prev) % 26 == 1
            # This handles both normal progression (a->b) and wraparound (z->a)
            if (ord(curr_char) - ord(prev_char)) % 26 == 1:
                # Extend the current valid substring
                current_length += 1
            else:
                # Start a new valid substring from current character
                current_length = 1
            
            # Update the maximum length for substrings ending with curr_char
            # We only keep the maximum because longer substrings contain all shorter ones
            max_len[curr_char] = max(max_len.get(curr_char, 0), current_length)
        
        # Sum all maximum lengths
        # Each character contributes as many unique substrings as the max length ending with it
        # E.g., if max length ending with 'c' is 3, we have 3 unique substrings ending with 'c'
        return sum(max_len.values())