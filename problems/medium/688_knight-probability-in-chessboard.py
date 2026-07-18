class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Knight's 8 possible moves in chess
        directions = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        # dp[r][c] represents the probability of being at (r, c) after i moves
        # We use two arrays to alternate between current and next state
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0  # Start position has probability 1
        
        # Simulate k moves
        for move in range(k):
            # Create new DP table for next move
            next_dp = [[0.0] * n for _ in range(n)]
            
            # For each cell on the board
            for r in range(n):
                for c in range(n):
                    # If there's any probability of being at this cell
                    if dp[r][c] > 0:
                        # Try all 8 knight moves
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            
                            # Check if new position is still on the board
                            if 0 <= nr < n and 0 <= nc < n:
                                # Each move has 1/8 probability of being chosen
                                # Add the contribution to the next cell
                                next_dp[nr][nc] += dp[r][c] / 8.0
            
            # Move to next state
            dp = next_dp
        
        # Sum all probabilities remaining on the board
        # After k moves, this gives us the probability of still being on board
        total_probability = sum(sum(row) for row in dp)
        
        return total_probability