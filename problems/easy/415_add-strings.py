class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Two pointers starting from the end of each string
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []
        
        # Process digits from right to left, handling different lengths
        while i >= 0 or j >= 0 or carry:
            # Get current digit or 0 if index out of bounds
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate sum of current position plus carry
            total = digit1 + digit2 + carry
            
            # Extract digit and new carry
            carry = total // 10
            digit = total % 10
            
            # Append current digit to result
            result.append(str(digit))
            
            # Move pointers left
            i -= 1
            j -= 1
        
        # Result is built in reverse order, so reverse it back
        return ''.join(reversed(result))