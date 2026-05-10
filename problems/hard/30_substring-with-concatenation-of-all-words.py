from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        # Edge case: concatenated substring longer than s
        if total_len > len(s):
            return []
        
        # Build frequency map of words to match against
        words_freq = Counter(words)
        result = []
        
        # We only need to start from offsets 0 to word_len-1
        # This covers all possible alignments of word boundaries
        for offset in range(word_len):
            # Sliding window approach for this offset
            left = offset
            right = offset
            current_freq = Counter()
            matched_count = 0  # Number of words matched in current window
            
            while right + word_len <= len(s):
                # Extract the word at the right pointer
                word = s[right:right + word_len]
                right += word_len
                
                if word in words_freq:
                    current_freq[word] += 1
                    matched_count += 1
                    
                    # If we have too many of this word, shrink from left
                    while current_freq[word] > words_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        matched_count -= 1
                        left += word_len
                    
                    # Check if we have a valid window
                    if matched_count == word_count:
                        result.append(left)
                        # Shrink window by one word from left to continue searching
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        matched_count -= 1
                        left += word_len
                else:
                    # Word not in words list, reset window
                    current_freq.clear()
                    matched_count = 0
                    left = right
        
        return result