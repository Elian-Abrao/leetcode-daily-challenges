from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Edge case: IP addresses need exactly 4 segments, each 1-3 digits
        # So valid string length is between 4 and 12
        if len(s) < 4 or len(s) > 12:
            return []
        
        result = []
        
        def is_valid_segment(segment: str) -> bool:
            # Check if a segment is valid for an IP address
            # Valid if: no leading zeros (except "0" itself), value <= 255
            if not segment:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return int(segment) <= 255
        
        def backtrack(start: int, path: List[str]):
            # Base case: if we have 4 segments and consumed entire string
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            # Pruning: if remaining segments can't fit remaining string
            remaining_segments = 4 - len(path)
            remaining_chars = len(s) - start
            # Each segment needs at least 1 char and at most 3 chars
            if remaining_chars < remaining_segments or remaining_chars > remaining_segments * 3:
                return
            
            # Try all possible segment lengths (1 to 3 digits)
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start:start + length]
                
                if is_valid_segment(segment):
                    path.append(segment)
                    backtrack(start + length, path)
                    path.pop()
        
        backtrack(0, [])
        return result