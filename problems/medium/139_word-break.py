from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict to set for O(1) lookup
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] represents whether s[0:i] can be segmented into dictionary words
        # Base case: empty string can always be segmented (vacuously true)
        dp = [False] * (n + 1)
        dp[0] = True
        
        # For each position i in string (1 to n inclusive)
        for i in range(1, n + 1):
            # Try all possible previous positions j where s[0:j] is valid
            for j in range(i):
                # If s[0:j] can be segmented AND s[j:i] is in dictionary
                # then s[0:i] can also be segmented
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check other j values once we found one
        
        # Return whether the entire string can be segmented
        return dp[n]