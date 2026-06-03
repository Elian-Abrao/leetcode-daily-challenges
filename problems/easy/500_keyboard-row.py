from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the three keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        # Store all three rows in a list for easier iteration
        rows = [row1, row2, row3]
        
        result = []
        
        # Check each word
        for word in words:
            # Convert to lowercase for case-insensitive comparison
            word_lower = word.lower()
            
            # Try to find which row contains all characters of this word
            for row in rows:
                # Check if all characters in the word belong to this row
                # We use set operations: if the set of word chars is a subset of row
                if set(word_lower).issubset(row):
                    result.append(word)
                    break  # No need to check other rows once we found a match
        
        return result