from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        # Helper function: compute (base^exp) % MOD using fast exponentiation
        def pow_mod(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if exp & 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp >>= 1
            return result
        
        # Key insight: decompose b digit by digit from left to right
        # If b = [d1, d2, ..., dn], then b = d1*10^(n-1) + d2*10^(n-2) + ... + dn
        # We can rewrite: a^b = a^(d1*10^(n-1) + ... + dn)
        # Process left-to-right: result = (result^10 * a^digit) % MOD
        # 
        # Example: b = [1,2,3] means 123
        # a^123 = a^(1*100 + 2*10 + 3)
        #       = a^(1*100) * a^(2*10) * a^3
        # 
        # Processing left to right:
        # Start: result = 1
        # After digit 1: result = a^1
        # After digit 2: result = (a^1)^10 * a^2 = a^(10+2) = a^12
        # After digit 3: result = (a^12)^10 * a^3 = a^(120+3) = a^123
        
        result = 1
        
        for digit in b:
            # Raise current result to the 10th power (shift left one decimal position)
            result = pow_mod(result, 10, MOD)
            # Multiply by a^digit
            result = (result * pow_mod(a, digit, MOD)) % MOD
        
        return result