from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        
        # Try all possible lengths for the first two numbers
        # The first number can be at most half the string (leaving room for at least 2 more numbers)
        for i in range(1, n):
            # Skip if first number has leading zero (except "0" itself)
            if num[0] == '0' and i > 1:
                break
            
            first = int(num[:i])
            # Check 32-bit constraint
            if first >= 2**31:
                break
            
            for j in range(i + 1, n):
                # Skip if second number has leading zero (except "0" itself)
                if num[i] == '0' and j - i > 1:
                    break
                
                second = int(num[i:j])
                # Check 32-bit constraint
                if second >= 2**31:
                    break
                
                # Try to build a Fibonacci sequence starting with first and second
                result = [first, second]
                pos = j
                
                # Keep trying to extend the sequence
                while pos < n:
                    # Calculate the expected next number
                    next_num = result[-1] + result[-2]
                    
                    # Check 32-bit constraint
                    if next_num >= 2**31:
                        break
                    
                    next_str = str(next_num)
                    next_len = len(next_str)
                    
                    # Check if remaining string starts with next_num
                    if pos + next_len > n:
                        break
                    
                    if num[pos:pos + next_len] == next_str:
                        result.append(next_num)
                        pos += next_len
                    else:
                        break
                
                # Check if we successfully consumed the entire string and have at least 3 numbers
                if pos == n and len(result) >= 3:
                    return result
        
        # No valid Fibonacci-like sequence found
        return []