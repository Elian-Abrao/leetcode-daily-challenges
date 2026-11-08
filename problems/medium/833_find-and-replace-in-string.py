from __future__ import annotations
from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        """
        Perform simultaneous replacements on string s.
        All replacements are non-overlapping per problem guarantee.
        
        Approach:
        1. For each operation, verify if source matches at the given index.
        2. Record valid replacements with their start index and replacement length.
        3. Build result by scanning s left-to-right, copying untouched segments
           and replacing matched substrings.
        
        Time: O(n + k) where n = len(s), k = number of operations.
        Space: O(n) for result construction.
        """
        n = len(s)
        k = len(indices)
        
        # Store replacement info for indices that are valid.
        # We'll use a dict keyed by start index for O(1) lookup during scan.
        # Value is (source_length, target_string)
        replacements: dict[int, tuple[int, str]] = {}
        
        for i in range(k):
            idx = indices[i]
            src = sources[i]
            src_len = len(src)
            
            # Verify source matches s at the given index
            # Edge case: ensure we don't read past string end
            if idx + src_len <= n and s[idx:idx + src_len] == src:
                replacements[idx] = (src_len, targets[i])
            # If no match, do nothing (skip this operation)
        
        # Build the result string by scanning s left to right
        result_parts: list[str] = []
        pos = 0
        
        while pos < n:
            if pos in replacements:
                src_len, tgt = replacements[pos]
                result_parts.append(tgt)
                pos += src_len  # Skip the original substring entirely
            else:
                # Copy original character
                result_parts.append(s[pos])
                pos += 1
        
        return ''.join(result_parts)