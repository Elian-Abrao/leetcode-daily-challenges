class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] = minimum cost to guarantee a win for range [i, j]
        # We use dynamic programming with a 2D table
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Build the table bottom-up by increasing range length
        # For ranges of length 1, cost is 0 (we know the answer)
        # We process ranges of increasing length
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                # Initialize to a large value
                dp[start][end] = float('inf')
                
                # Try each possible guess k in the range [start, end]
                for k in range(start, end + 1):
                    # Cost if we guess k:
                    # - We pay k dollars
                    # - If actual number is in [start, k-1], we pay dp[start][k-1]
                    # - If actual number is in [k+1, end], we pay dp[k+1][end]
                    # We must guarantee a win, so take the worst case (max)
                    
                    # Handle edge cases where left or right subrange doesn't exist
                    left_cost = dp[start][k - 1] if k > start else 0
                    right_cost = dp[k + 1][end] if k < end else 0
                    
                    # The worst case cost if we guess k
                    worst_case = k + max(left_cost, right_cost)
                    
                    # We want to minimize the worst case cost across all guesses
                    dp[start][end] = min(dp[start][end], worst_case)
        
        return dp[1][n]