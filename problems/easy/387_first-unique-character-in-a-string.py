class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Use a frequency map to count occurrences of each character
        # Time: O(n) for building the map, Space: O(1) since at most 26 lowercase letters
        freq = {}
        
        # First pass: count frequency of each character
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Second pass: find the first character with frequency 1
        # We iterate through the string (not the map) to preserve order
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        
        # No unique character found
        return -1