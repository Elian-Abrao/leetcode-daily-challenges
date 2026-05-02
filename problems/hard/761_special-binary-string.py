class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case: minimal special string
        if len(s) <= 2:
            return s
        
        # Find all consecutive special substrings at the current level
        # These are substrings where balance (count of 1s - count of 0s) returns to 0
        substrings = []
        balance = 0
        start = 0
        
        for i in range(len(s)):
            # Treat '1' as +1 and '0' as -1
            if s[i] == '1':
                balance += 1
            else:
                balance -= 1
            
            # When balance returns to 0, we found a complete special substring
            if balance == 0:
                # Extract the special substring
                substring = s[start:i+1]
                
                # For each special substring "1...0", recursively process the interior
                # The interior is everything between the outer '1' and '0'
                if len(substring) > 2:
                    # Remove outer '1' and '0', recursively optimize interior
                    inner = substring[1:-1]
                    optimized_inner = self.makeLargestSpecial(inner)
                    # Wrap it back with '1' and '0'
                    substring = '1' + optimized_inner + '0'
                
                substrings.append(substring)
                start = i + 1
        
        # Sort substrings in descending order for lexicographically largest result
        # Larger strings (lexicographically) should come first
        substrings.sort(reverse=True)
        
        # Concatenate all sorted substrings
        return ''.join(substrings)