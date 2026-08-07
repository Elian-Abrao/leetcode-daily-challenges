class Solution:
    def lastSubstring(self, s: str) -> str:
        # Goal: Find the lexicographically largest suffix of s
        # Key insight: The answer is always a suffix (substring from some index to end)
        # because extending any substring to the end can only increase or maintain its lex order
        
        # We use a two-pointer approach to efficiently compare candidate starting positions
        # Time: O(n), Space: O(1)
        
        n = len(s)
        if n == 1:
            return s
        
        # i: current best candidate starting position
        # j: competing candidate starting position
        # k: offset for comparing characters at positions i+k and j+k
        i = 0
        j = 1
        k = 0
        
        while j + k < n:
            if s[i + k] == s[j + k]:
                # Characters match, extend comparison
                k += 1
            elif s[i + k] > s[j + k]:
                # s[i:] is better than s[j:], discard j
                # Jump j past the failed match since any position between j and j+k
                # would be dominated by either i or j+k+1
                j = j + k + 1
                k = 0
            else:
                # s[j:] is better than s[i:], update i to j
                # Similarly, any position between i and i+k is dominated
                # Move i to the position after the mismatch or to j, whichever is further
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
        
        return s[i:]