from __future__ import annotations
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list for empty input
        if not digits:
            return []
        
        # Digit to letters mapping as on a phone keypad
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        # Start with an empty string to simplify concatenation
        combinations: List[str] = ['']
        
        # For each digit, expand current combinations with its possible letters
        for d in digits:
            letters = digit_to_letters[d]
            next_combinations: List[str] = []
            for prefix in combinations:
                for ch in letters:
                    next_combinations.append(prefix + ch)
            combinations = next_combinations
        
        return combinations