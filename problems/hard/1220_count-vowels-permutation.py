class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Map vowels to indices: a=0, e=1, i=2, o=3, u=4
        # Define transition rules based on problem constraints:
        # 'a' -> 'e'
        # 'e' -> 'a', 'i'
        # 'i' -> 'a', 'e', 'o', 'u' (all except 'i')
        # 'o' -> 'i', 'u'
        # 'u' -> 'a'
        
        # dp[i] represents count of strings of current length ending with vowel i
        # Initialize: for length 1, each vowel can appear once
        dp = [1, 1, 1, 1, 1]  # [a, e, i, o, u]
        
        # Build strings of increasing length from 2 to n
        for length in range(2, n + 1):
            # Calculate new counts based on which vowels can precede each vowel
            # new_a: strings ending in 'a' come from 'e', 'i', 'u'
            # new_e: strings ending in 'e' come from 'a', 'i'
            # new_i: strings ending in 'i' come from 'e', 'o'
            # new_o: strings ending in 'o' come from 'i'
            # new_u: strings ending in 'u' come from 'i', 'o'
            
            new_a = (dp[1] + dp[2] + dp[4]) % MOD  # e, i, u -> a
            new_e = (dp[0] + dp[2]) % MOD           # a, i -> e
            new_i = (dp[1] + dp[3]) % MOD           # e, o -> i
            new_o = dp[2]                           # i -> o
            new_u = (dp[2] + dp[3]) % MOD           # i, o -> u
            
            # Update dp array for next iteration
            dp = [new_a, new_e, new_i, new_o, new_u]
        
        # Sum all possible strings of length n ending with any vowel
        return sum(dp) % MOD