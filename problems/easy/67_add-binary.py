class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Use two pointers starting from the end of both strings
        # Simulate binary addition with carry propagation
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        
        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get current bit from a (or 0 if exhausted)
            bit_a = int(a[i]) if i >= 0 else 0
            # Get current bit from b (or 0 if exhausted)
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum of current bits plus carry
            total = bit_a + bit_b + carry
            
            # Current bit is total % 2
            result.append(str(total % 2))
            
            # Carry for next position is total // 2
            carry = total // 2
            
            # Move pointers left
            i -= 1
            j -= 1
        
        # Result was built in reverse order, so reverse it back
        return ''.join(reversed(result))