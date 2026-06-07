class Solution:
    def largestPalindrome(self, n: int) -> int:
        # Edge case: for n=1, the largest product is 9*9=81, but largest palindrome is 9
        # Actually for n=1, we want max palindrome from products of 1-digit numbers
        # 9*9=81 is not palindrome, but 9*1=9 is. The largest is 9.
        if n == 1:
            return 9
        
        # Define the range of n-digit numbers
        upper = 10**n - 1  # largest n-digit number (e.g., 99 for n=2)
        lower = 10**(n-1)  # smallest n-digit number (e.g., 10 for n=2)
        
        # We search for palindromes from largest to smallest
        # A palindrome product of two n-digit numbers will have at most 2n digits
        # We construct palindrome candidates by mirroring the first half
        
        # Start from the largest possible first half
        max_first_half = upper
        
        for first_half in range(max_first_half, lower - 1, -1):
            # Create palindrome by mirroring first_half
            palindrome = self._create_palindrome(first_half)
            
            # Check if this palindrome can be expressed as product of two n-digit numbers
            # We only need to check divisors from upper down to sqrt(palindrome)
            # But we constrain both factors to be n-digit numbers
            for i in range(upper, lower - 1, -1):
                # If i*i < palindrome, no point checking further
                if i * i < palindrome:
                    break
                
                # Check if palindrome is divisible by i
                if palindrome % i == 0:
                    other = palindrome // i
                    # Check if other factor is also an n-digit number
                    if lower <= other <= upper:
                        return palindrome % 1337
        
        # Should not reach here given constraints
        return 0
    
    def _create_palindrome(self, first_half: int) -> int:
        # Create a palindrome by mirroring first_half
        # E.g., 99 -> 9009
        s = str(first_half)
        palindrome_str = s + s[::-1]
        return int(palindrome_str)