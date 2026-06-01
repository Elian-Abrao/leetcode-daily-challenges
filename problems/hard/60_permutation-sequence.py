class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Precompute factorials up to (n-1)!
        # factorial[i] = i!
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        
        # List of available digits (1 to n)
        digits = list(range(1, n + 1))
        
        # Convert k to 0-indexed for easier calculation
        k -= 1
        
        result = []
        
        # Build the permutation digit by digit
        for i in range(n):
            # Number of positions left to fill after this one
            # For each remaining position, there are factorial[n-1-i] permutations
            fact = factorial[n - 1 - i]
            
            # Determine which digit to pick from available digits
            # index tells us which of the remaining digits to use
            index = k // fact
            
            # Add the chosen digit to result
            result.append(str(digits[index]))
            
            # Remove the used digit from available digits
            digits.pop(index)
            
            # Update k to represent position within the sub-problem
            # We've "used up" index * fact permutations
            k %= fact
        
        return ''.join(result)