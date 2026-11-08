from collections import Counter
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # Convert each word to a bitmask of its unique letters (max 26 bits).
        # This is the core idea: we only care about which letters appear, not their frequency.
        # Since word length is up to 50, duplicates don't matter for the bitmask.
        
        word_mask_counts = Counter()
        for w in words:
            mask = 0
            # Set bit for each character in the word
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            # Only count the mask once; duplicates don't affect validity.
            word_mask_counts[mask] += 1
        
        result = []
        
        for puzzle in puzzles:
            # The puzzle string has exactly 7 distinct characters.
            # Build a bitmask for the puzzle.
            puzzle_mask = 0
            for ch in puzzle:
                puzzle_mask |= 1 << (ord(ch) - ord('a'))
            
            first_char_bit = 1 << (ord(puzzle[0]) - ord('a'))
            
            # We will iterate over all submask of puzzle_mask that INCLUDE the first letter.
            # This is the standard trick: iterate over submasks of a given mask efficiently.
            # Start from puzzle_mask and go down, but ensure first_char_bit is always set.
            
            # We can use a common technique: iterate submask = puzzle_mask; then submask = (submask-1) & puzzle_mask.
            # However, we must only count masks that have first_char_bit set.
            # Equivalent: consider submask = puzzle_mask; while True: ...; then submask = (submask-1)&puzzle_mask; break if submask == 0 after.
            # But we can just skip those without first_char_bit.
            
            count = 0
            submask = puzzle_mask
            while True:
                # If submask contains the first letter, count matches
                if (submask & first_char_bit) != 0:
                    count += word_mask_counts.get(submask, 0)
                
                # If submask is 0, we are done
                if submask == 0:
                    break
                
                # Move to next submask (this enumerates all subsets of puzzle_mask)
                submask = (submask - 1) & puzzle_mask
            
            result.append(count)
        
        return result