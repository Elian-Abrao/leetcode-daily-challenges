class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        
        # Result can have at most m + n digits
        # Example: 99 * 99 = 9801 (2 + 2 = 4 digits)
        result = [0] * (m + n)
        
        # Iterate from right to left (least significant digit first)
        for i in range(m - 1, -1, -1):
            digit1 = int(num1[i])
            
            for j in range(n - 1, -1, -1):
                digit2 = int(num2[j])
                
                # Multiply current digits
                mul = digit1 * digit2
                
                # Position in result array where this product contributes
                # i + j + 1 is the lower position, i + j is the higher position
                pos1 = i + j
                pos2 = i + j + 1
                
                # Add multiplication result to existing value at pos2
                mul += result[pos2]
                
                # Store the ones place at pos2
                result[pos2] = mul % 10
                
                # Add carry to the higher position
                result[pos1] += mul // 10
        
        # Convert result array to string, skipping leading zeros
        # Start from index 0, but skip if it's 0 (can happen when result has fewer than m+n digits)
        result_str = ''.join(map(str, result))
        
        # Remove leading zeros (though by construction we shouldn't have many)
        # Since we handle "0" case above, we're safe to strip
        return result_str.lstrip('0') or '0'