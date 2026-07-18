class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Key insight: The problem behavior changes drastically based on k
        
        # Case 1: k == 1
        # We can only move the first character to the end repeatedly.
        # This is equivalent to rotating the string.
        # We can only achieve the n rotations of the original string.
        # Return the lexicographically smallest rotation.
        
        # Case 2: k >= 2
        # With k >= 2, we can achieve ANY permutation of the string.
        # Proof: With k=2, we can swap adjacent elements:
        #   - Move first char to end: "abc" -> "bca"
        #   - Move first char to end: "bca" -> "cab"
        #   - Move first char to end: "cab" -> "abc"
        #   - By carefully choosing which of the first 2 chars to move,
        #     we can bubble sort and achieve any permutation.
        # Therefore, return the sorted string (lexicographically smallest permutation).
        
        if k == 1:
            # Find the lexicographically smallest rotation
            # We generate all n rotations and pick the smallest
            n = len(s)
            min_rotation = s
            
            # Try all possible rotations
            for i in range(1, n):
                # Rotation by i positions: s[i:] + s[:i]
                rotation = s[i:] + s[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            
            return min_rotation
        else:
            # k >= 2: we can achieve any permutation
            # Return the sorted string (lexicographically smallest)
            return ''.join(sorted(s))