from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Key insight: use bitmask to represent character set of each word
        # Two words share no common letters iff their bitmasks have no overlapping bits
        # This allows O(1) check using bitwise AND operation
        
        n = len(words)
        
        # Precompute bitmask for each word
        # bit i is set if character ('a' + i) is present in the word
        masks = []
        for word in words:
            mask = 0
            for char in word:
                # Set the bit corresponding to this character
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)
        
        max_product = 0
        
        # Check all pairs of words
        # O(n^2) comparison but each check is O(1) thanks to bitmask
        for i in range(n):
            for j in range(i + 1, n):
                # If bitwise AND is 0, no common characters
                if masks[i] & masks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        
        return max_product