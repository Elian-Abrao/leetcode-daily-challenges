from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Edge case: if string is shorter than 10, no 10-letter sequences exist
        if len(s) < 10:
            return []
        
        # Track all seen 10-letter sequences and those that appear more than once
        seen = set()
        repeated = set()
        
        # Sliding window approach: examine each 10-letter substring
        # Time: O(n) where n = len(s), each substring operation is O(10) = O(1)
        # Space: O(n) in worst case if all substrings are unique
        for i in range(len(s) - 9):
            # Extract current 10-letter sequence
            sequence = s[i:i+10]
            
            # If we've seen this sequence before, it's a repeat
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        
        # Convert set to list for return (order doesn't matter per problem statement)
        return list(repeated)