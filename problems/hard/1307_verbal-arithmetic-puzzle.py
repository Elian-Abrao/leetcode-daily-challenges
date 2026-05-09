from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Collect all unique characters
        chars = set()
        for word in words:
            chars.update(word)
        chars.update(result)
        chars = list(chars)
        
        # If more than 10 unique characters, impossible to map to digits 0-9
        if len(chars) > 10:
            return False
        
        # Identify characters that cannot be zero (leading characters)
        leading = set()
        for word in words:
            if len(word) > 1:
                leading.add(word[0])
        if len(result) > 1:
            leading.add(result[0])
        
        # Precompute coefficients for each character
        # For addition: sum(words) = result
        # We rearrange to: sum(words) - result = 0
        coeff = {}
        for ch in chars:
            coeff[ch] = 0
        
        # Add positive coefficients from words
        for word in words:
            multiplier = 1
            for ch in reversed(word):
                coeff[ch] += multiplier
                multiplier *= 10
        
        # Subtract coefficients from result
        multiplier = 1
        for ch in reversed(result):
            coeff[ch] -= multiplier
            multiplier *= 10
        
        # Backtracking to assign digits to characters
        char_to_digit = {}
        used_digits = set()
        
        def backtrack(idx):
            # Base case: all characters assigned
            if idx == len(chars):
                # Check if the equation holds
                total = sum(coeff[ch] * char_to_digit[ch] for ch in chars)
                return total == 0
            
            ch = chars[idx]
            # Try assigning each digit 0-9 to current character
            for digit in range(10):
                # Skip if digit already used
                if digit in used_digits:
                    continue
                # Skip if character is leading and digit is 0
                if digit == 0 and ch in leading:
                    continue
                
                # Assign digit to character
                char_to_digit[ch] = digit
                used_digits.add(digit)
                
                # Recurse to next character
                if backtrack(idx + 1):
                    return True
                
                # Backtrack
                del char_to_digit[ch]
                used_digits.remove(digit)
            
            return False
        
        return backtrack(0)