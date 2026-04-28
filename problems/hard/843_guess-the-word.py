from typing import List
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match_count(w1: str, w2: str) -> int:
            """Count exact character matches between two words at same positions."""
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))
        
        # Keep track of candidate words
        candidates = words[:]
        
        # Iterate up to 10 guesses (problem guarantees solution within allowed guesses)
        for _ in range(10):
            # Strategy: Pick word that minimizes worst-case elimination
            # We want a word that has good overlap distribution with remaining candidates
            
            # Heuristic: Choose the word that minimizes the maximum group size
            # after partitioning candidates by match count
            best_word = None
            min_worst_case = float('inf')
            
            # Optimization: Sample a subset if candidate list is large
            sample_size = min(len(candidates), 20)
            sample = random.sample(candidates, sample_size)
            
            for word in sample:
                # For this candidate word, simulate what happens if we guess it
                # Group all other candidates by their match count with this word
                match_groups = [0] * 7  # 0 to 6 matches possible
                
                for candidate in candidates:
                    if candidate != word:
                        matches = match_count(word, candidate)
                        match_groups[matches] += 1
                
                # Worst case: largest group size (most candidates we might retain)
                worst_case = max(match_groups)
                
                # Pick word with smallest worst-case scenario
                if worst_case < min_worst_case:
                    min_worst_case = worst_case
                    best_word = word
            
            # If heuristic fails, just pick first candidate
            if best_word is None:
                best_word = candidates[0]
            
            # Make the guess
            matches = master.guess(best_word)
            
            # If we found the secret word, we're done
            if matches == 6:
                return
            
            # Filter candidates: keep only words with same match count to our guess
            # Key insight: if guess has X matches with secret, then secret must have
            # X matches with guess. So we eliminate all words that don't have X matches.
            candidates = [
                word for word in candidates 
                if match_count(word, best_word) == matches
            ]
            
            # Edge case: if no candidates remain, something went wrong
            # (shouldn't happen with valid input)
            if not candidates:
                return