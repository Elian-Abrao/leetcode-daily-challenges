class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: first term in the sequence
        if n == 1:
            return "1"
        
        # Start with the base case and iteratively build up to the nth term
        current = "1"
        
        # Generate each subsequent term from term 2 to term n
        for i in range(2, n + 1):
            current = self._getNextTerm(current)
        
        return current
    
    def _getNextTerm(self, s: str) -> str:
        """
        Generate the next term in the count-and-say sequence by performing
        run-length encoding on the current string.
        
        Args:
            s: Current term in the sequence
            
        Returns:
            Next term obtained by encoding consecutive runs of digits
        """
        # Use a list for efficient string building (O(1) append vs O(n) concat)
        result = []
        i = 0
        
        # Process each run of consecutive identical digits
        while i < len(s):
            current_digit = s[i]
            count = 1
            
            # Count consecutive occurrences of the current digit
            while i + count < len(s) and s[i + count] == current_digit:
                count += 1
            
            # Append count followed by the digit itself
            # Format: "count" + "digit"
            result.append(str(count))
            result.append(current_digit)
            
            # Move to the next different digit
            i += count
        
        return ''.join(result)