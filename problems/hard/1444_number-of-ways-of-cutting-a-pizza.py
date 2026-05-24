from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows = len(pizza)
        cols = len(pizza[0])
        
        # Precompute suffix sum of apples from each position (r, c) to bottom-right
        # apples[r][c] = number of apples in rectangle from (r, c) to (rows-1, cols-1)
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
                if pizza[r][c] == 'A':
                    apples[r][c] += 1
        
        # Memoization: dp[r][c][cuts_remaining] = ways to cut pizza[r:][c:] with cuts_remaining cuts
        memo = {}
        
        def dp(r, c, cuts_remaining):
            # Base case: no more cuts needed
            if cuts_remaining == 0:
                # Check if current piece has at least one apple
                return 1 if apples[r][c] > 0 else 0
            
            # Check memo
            if (r, c, cuts_remaining) in memo:
                return memo[(r, c, cuts_remaining)]
            
            # If no apples in remaining pizza, no valid way
            if apples[r][c] == 0:
                memo[(r, c, cuts_remaining)] = 0
                return 0
            
            result = 0
            
            # Try horizontal cuts: cut between row i and i+1, give upper part away
            for i in range(r, rows - 1):
                # Upper piece is pizza[r:i+1][c:], check if it has apples
                upper_apples = apples[r][c] - apples[i + 1][c]
                if upper_apples > 0:
                    # Recursively count ways for bottom piece starting at (i+1, c)
                    result = (result + dp(i + 1, c, cuts_remaining - 1)) % MOD
            
            # Try vertical cuts: cut between column j and j+1, give left part away
            for j in range(c, cols - 1):
                # Left piece is pizza[r:][c:j+1], check if it has apples
                left_apples = apples[r][c] - apples[r][j + 1]
                if left_apples > 0:
                    # Recursively count ways for right piece starting at (r, j+1)
                    result = (result + dp(r, j + 1, cuts_remaining - 1)) % MOD
            
            memo[(r, c, cuts_remaining)] = result
            return result
        
        # Start with full pizza at (0, 0) and need k-1 cuts (to create k pieces)
        return dp(0, 0, k - 1)