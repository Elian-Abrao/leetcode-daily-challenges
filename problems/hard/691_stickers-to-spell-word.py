from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert stickers to character frequency counters for efficient lookup
        sticker_counts = [Counter(s) for s in stickers]
        
        # Preprocess: Remove stickers that don't contribute any unique letters
        # and keep only letters that appear in target
        target_set = set(target)
        sticker_counts = [
            {c: cnt for c, cnt in counter.items() if c in target_set}
            for counter in sticker_counts
        ]
        # Remove empty stickers after filtering
        sticker_counts = [s for s in sticker_counts if s]
        
        # Early check: if any character in target is not available in any sticker
        available_chars = set()
        for counter in sticker_counts:
            available_chars.update(counter.keys())
        for char in target:
            if char not in available_chars:
                return -1
        
        # Use memoization with string representation of remaining target
        # State: remaining characters to spell
        @lru_cache(maxsize=None)
        def dp(remaining: str) -> int:
            # Base case: all characters spelled
            if not remaining:
                return 0
            
            # Count frequency of remaining characters
            remaining_count = Counter(remaining)
            
            min_stickers = float('inf')
            
            # Try using each sticker
            for sticker in sticker_counts:
                # Optimization: only consider stickers that have the first char
                # This prevents exploring redundant states where we cycle through
                # stickers that don't contribute to progress
                if remaining[0] not in sticker:
                    continue
                
                # Build new remaining string after using this sticker
                new_remaining_list = []
                for char in remaining:
                    # Use up characters from current sticker if available
                    if remaining_count[char] > 0:
                        if sticker.get(char, 0) > 0:
                            sticker[char] -= 1
                        else:
                            new_remaining_list.append(char)
                        remaining_count[char] -= 1
                
                # Restore sticker counts (since dict is mutable)
                for char in remaining:
                    if char in sticker:
                        sticker[char] = Counter(stickers[sticker_counts.index(sticker)])[char]
                
                # Actually use immutable approach: recompute what remains
                new_remaining_chars = []
                sticker_copy = sticker.copy()
                for char in remaining:
                    if sticker_copy.get(char, 0) > 0:
                        sticker_copy[char] -= 1
                    else:
                        new_remaining_chars.append(char)
                
                new_remaining = ''.join(new_remaining_chars)
                
                # Recursively solve for new remaining string
                result = dp(new_remaining)
                if result != -1:
                    min_stickers = min(min_stickers, 1 + result)
            
            # Return -1 if impossible, otherwise return minimum
            return min_stickers if min_stickers != float('inf') else -1
        
        return dp(target)