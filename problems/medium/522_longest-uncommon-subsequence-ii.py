class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        # Key insight: if a string s is a subsequence of another string t,
        # then s cannot be an uncommon subsequence because any subsequence
        # of s is also a subsequence of t. The longest uncommon subsequence
        # will be one of the original strings (since strings themselves are
        # subsequences of themselves), and we must verify it's not a subsequence
        # of any other string.
        
        def is_subsequence(a: str, b: str) -> bool:
            """Check if string a is a subsequence of string b."""
            it = iter(b)
            # Greedy matching: for each char in a, find it in b sequentially
            return all(char in it for char in a)
        
        # Sort by length descending: longer strings have higher potential
        # to be uncommon subsequences
        strs.sort(key=len, reverse=True)
        
        n = len(strs)
        
        for i in range(n):
            # For each string, check if it's a subsequence of any other string
            is_uncommon = True
            for j in range(n):
                if i == j:
                    continue
                # Only need to check if strs[i] is subsequence of a longer or equal string
                # since shorter strings can't contain longer subsequences
                if len(strs[i]) > len(strs[j]):
                    continue
                if is_subsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(strs[i])
        
        # No uncommon subsequence found (all strings are subsequences of others)
        return -1