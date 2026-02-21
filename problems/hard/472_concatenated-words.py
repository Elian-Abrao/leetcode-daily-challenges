from __future__ import annotations
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)  # Quick lookup for words
        res: List[str] = []
        
        for w in words:
            if not w:
                continue
            memo = {}  # Memoization for can_form on substrings
            
            def can_form(s: str) -> bool:
                # Returns True if s can be formed by concatenating one or more words from word_set
                if s in memo:
                    return memo[s]
                if s in word_set:
                    memo[s] = True
                    return True
                # Try to split s into left and right parts
                for i in range(1, len(s)):
                    if s[:i] in word_set and can_form(s[i:]):
                        memo[s] = True
                        return True
                memo[s] = False
                return False
            
            # Check if w can be split into at least two words:
            # left part w[:i] must be a word, and the remainder w[i:] must be formable
            for i in range(1, len(w)):
                if w[:i] in word_set and can_form(w[i:]):
                    res.append(w)
                    break
        
        return res