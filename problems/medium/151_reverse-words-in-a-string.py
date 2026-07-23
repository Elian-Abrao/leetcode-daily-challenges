class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by whitespace automatically handles multiple spaces and strips leading/trailing
        # split() with no argument splits on any whitespace and removes empty strings
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join with single space
        return ' '.join(words)