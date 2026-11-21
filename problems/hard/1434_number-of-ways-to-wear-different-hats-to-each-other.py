from __future__ import annotations
from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = len(hats)                     # number of people, ≤ 10
        HAT_TYPES = 40                    # fixed constraint
        
        # For each hat (1..40), store which people prefer it.
        # Using 0-based indexing for people.
        hat_to_people: List[List[int]] = [[] for _ in range(HAT_TYPES + 1)]
        for person, preferred in enumerate(hats):
            for h in preferred:
                hat_to_people[h].append(person)
        
        # dp[mask] = number of ways to assign hats to people represented by mask
        # Size: 1 << n (max 1024)
        dp = [0] * (1 << n)
        dp[0] = 1                         # empty assignment
        
        # Process hats one by one to avoid counting the same hat multiple times
        for hat in range(1, HAT_TYPES + 1):
            # Only need to consider people who like this hat
            people = hat_to_people[hat]
            if not people:
                continue
            
            # Iterate masks in descending order to avoid reusing the same hat
            for mask in range((1 << n) - 1, -1, -1):
                # Skip masks that are impossible (0 ways) — minor optimization
                if dp[mask] == 0:
                    continue
                
                # Try giving this hat to any person who likes it and is not yet assigned
                for p in people:
                    if mask & (1 << p):
                        continue          # person already has a hat
                    new_mask = mask | (1 << p)
                    dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD
        
        # All people assigned = mask with n ones
        return dp[(1 << n) - 1] % MOD