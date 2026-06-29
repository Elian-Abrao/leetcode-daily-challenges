class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base case: if string is too short, it can't satisfy the condition
        if len(s) < k:
            return 0
        
        # Strategy: Divide and conquer approach
        # Key insight: if a character appears less than k times in the entire string,
        # it cannot be part of any valid substring. We can split on such characters.
        
        # Count frequency of each character in the string
        from collections import Counter
        counter = Counter(s)
        
        # Find characters that appear less than k times
        # These act as "invalid" separators
        for char, count in counter.items():
            if count < k:
                # Split the string by this invalid character
                # Recursively find the longest valid substring in each partition
                max_len = 0
                for substring in s.split(char):
                    max_len = max(max_len, self.longestSubstring(substring, k))
                return max_len
        
        # If we reach here, all characters in s appear at least k times
        # This means the entire string is valid
        return len(s)