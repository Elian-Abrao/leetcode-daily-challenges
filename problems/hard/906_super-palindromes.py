import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # Convert the input strings to integers
        L = int(left)
        R = int(right)
        
        # The maximum possible root of a super-palindrome is sqrt(R)
        limit = math.isqrt(R)
        count = 0
        
        # All palindromes up to 'limit' can be constructed from halves.
        # The largest palindrome ≤ 10^9 has 9 digits, so its half has 5 digits.
        # We compute the maximum half length needed.
        half_max = 10 ** ((len(str(limit)) + 1) // 2)  # exclusive upper bound
        
        for half in range(1, half_max):
            s = str(half)
            
            # --- Odd-length palindrome ---
            # e.g., half = "123"  →  "12321"
            odd_str = s + s[-2::-1]          # s without last char, reversed
            p = int(odd_str)
            if p <= limit:
                sq = p * p
                if L <= sq <= R:
                    sq_str = str(sq)
                    if sq_str == sq_str[::-1]:
                        count += 1
            
            # --- Even-length palindrome ---
            # e.g., half = "123"  →  "123321"
            even_str = s + s[::-1]
            p = int(even_str)
            if p <= limit:
                sq = p * p
                if L <= sq <= R:
                    sq_str = str(sq)
                    if sq_str == sq_str[::-1]:
                        count += 1
        
        return count