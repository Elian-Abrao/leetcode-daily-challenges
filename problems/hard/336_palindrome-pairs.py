from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Core insight: For words[i] + words[j] to be palindrome:
        # Case 1: len(words[i]) == len(words[j]) -> words[j] must be reverse of words[i]
        # Case 2: len(words[i]) < len(words[j]) -> 
        #   Split words[j] into left + right where len(right) == len(words[i])
        #   If right is reverse of words[i] AND left is palindrome, then valid
        # Case 3: len(words[i]) > len(words[j]) ->
        #   Split words[i] into left + right where len(left) == len(words[j])
        #   If left is reverse of words[j] AND right is palindrome, then valid
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        # Build a map from word to its index for O(1) lookup
        word_map = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            word_len = len(word)
            
            # For each word, try all possible splits
            # k represents the split position: word[:k] and word[k:]
            for k in range(word_len + 1):
                left = word[:k]
                right = word[k:]
                
                # Case 1: left part is palindrome
                # Check if reverse of right exists
                # This handles: reverse(right) + word = palindrome
                # because reverse(right) + left + right -> reverse(right) + (left as palindrome) + right
                if is_palindrome(left):
                    right_rev = right[::-1]
                    if right_rev in word_map and word_map[right_rev] != i:
                        j = word_map[right_rev]
                        result.append([j, i])
                
                # Case 2: right part is palindrome
                # Check if reverse of left exists
                # This handles: word + reverse(left) = palindrome
                # because left + right + reverse(left) -> left + (right as palindrome) + reverse(left)
                # Special condition: k != word_len to avoid duplicate with case 1 when k=len(word)
                # (when k=len, right="" which is palindrome, would cause duplicate checking)
                if k != word_len and is_palindrome(right):
                    left_rev = left[::-1]
                    if left_rev in word_map and word_map[left_rev] != i:
                        j = word_map[left_rev]
                        result.append([i, j])
        
        return result