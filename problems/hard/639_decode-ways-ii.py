class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] = number of ways to decode s[0:i]
        # We only need the last two values to save space.
        prev2 = 1  # dp[0] = 1 (empty string)
        prev1 = self._count_single(s[0])  # dp[1] = ways to decode first char
        
        if n == 1:
            return prev1 % MOD
        
        for i in range(1, n):
            curr = 0
            
            # Case 1: decode current character alone
            single_ways = self._count_single(s[i])
            curr = (curr + prev1 * single_ways) % MOD
            
            # Case 2: decode current and previous as a two-digit group
            double_ways = self._count_double(s[i-1], s[i])
            curr = (curr + prev2 * double_ways) % MOD
            
            # Shift dp window forward
            prev2, prev1 = prev1, curr
        
        return prev1 % MOD
    
    def _count_single(self, ch: str) -> int:
        """Number of ways to decode a single character."""
        if ch == '*':
            # '*' represents 1-9 → 9 possible digits, each decodes to one letter
            return 9
        elif ch == '0':
            # '0' cannot be decoded alone
            return 0
        else:
            # '1'-'9' each decodes to one letter
            return 1
    
    def _count_double(self, first: str, second: str) -> int:
        """Number of ways to decode a two-character group (first + second)."""
        # This group must be a valid two-digit number 10-26
        
        if first == '*' and second == '*':
            # ** -> possibilities: 11-19 (9 ways) and 21-26 (6 ways) = 15 total
            # But 20 is not possible because second != 0? Actually second * is 1-9, so 10-19 and 20-26? 
            # Wait, second is *, so digits 1-9. Combined with first digits 1-9:
            # First * = 1-9. Valid two-digit numbers: 11-19 (9 ways) and 21-26 (6 ways) = 15
            return 15
            
        elif first == '*':
            # * + digit: first can be 1 or 2 to form 10-26
            d = int(second)
            if 0 <= d <= 6:
                # If second is 0-6, first can be 1 or 2 (10-16 or 20-26)
                return 2
            else:
                # second is 7-9, first can only be 1 (17-19)
                return 1
                
        elif second == '*':
            # digit + *: second can be 1-9
            f = int(first)
            if f == 1:
                # 1* -> 11-19 → 9 possibilities
                return 9
            elif f == 2:
                # 2* -> 21-26 → 6 possibilities (20 is invalid because * != 0)
                return 6
            else:
                # anything else (0, 3-9) cannot form valid two-digit numbers
                return 0
                
        else:
            # Both are digits
            num = int(first) * 10 + int(second)
            if 10 <= num <= 26:
                return 1
            return 0