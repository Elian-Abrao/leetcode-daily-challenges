class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sliding window with a hash map to track the last seen index of each character
        # Time: O(n), Space: O(min(n, m)) where m is the charset size
        
        # Handle edge case: empty string
        if not s:
            return 0
        
        # Map each character to its most recent index in the string
        char_index = {}
        
        # left pointer marks the start of the current window without duplicates
        left = 0
        max_length = 0
        
        # Expand the window by moving right pointer
        for right in range(len(s)):
            char = s[right]
            
            # If char was seen before and is within the current window,
            # move left pointer to exclude the previous occurrence
            if char in char_index and char_index[char] >= left:
                # Move left to one position after the last occurrence of char
                left = char_index[char] + 1
            
            # Update the last seen index of the current character
            char_index[char] = right
            
            # Calculate current window size and update max if needed
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length