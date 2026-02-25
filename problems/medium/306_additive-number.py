class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        Check if the given string can form an additive sequence.
        We iterate over possible first and second numbers,
        then greedily verify the rest by matching the sum as a prefix.
        Leading zeros are invalid for numbers with length > 1.
        """
        n = len(num)
        if n < 3:
            return False  # At least three numbers required
        
        # Try all possible lengths for the first number
        for i in range(1, n - 1):
            # First number cannot have leading zeros unless it is "0"
            if num[0] == '0' and i > 1:
                break  # All longer first numbers will also be invalid
            a = int(num[:i])
            
            # Try all possible lengths for the second number
            for j in range(i + 1, n):
                # Second number cannot have leading zeros unless it is "0"
                if num[i] == '0' and (j - i) > 1:
                    break  # All longer second numbers invalid for this i
                b = int(num[i:j])
                
                # Validate the rest of the sequence
                k = j  # position to check next number
                x, y = a, b  # the last two numbers in the sequence
                while k < n:
                    s = x + y
                    s_str = str(s)
                    # Check if next piece of string matches the sum
                    if not num.startswith(s_str, k):
                        break
                    k += len(s_str)
                    x, y = y, s
                if k == n:
                    return True
        
        return False