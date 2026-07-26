from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Use DP working backwards from princess to knight
        # dp[i][j] = minimum HP needed when ENTERING cell (i, j) to reach princess
        # Key insight: we must work backwards because the constraint is about
        # maintaining HP > 0 at ALL times, not just at the end
        
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] represents the minimum health required when entering cell (i,j)
        # to guarantee survival to the end
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Base case: at princess cell, we need enough HP to survive that cell
        # After taking damage/heal from dungeon[m-1][n-1], HP must be at least 1
        # So before entering: HP >= 1 - dungeon[m-1][n-1]
        # But HP must also be at least 1 to start with
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill last column (can only come from below, but we're going backwards)
        # Going backwards means: from cell (i,j) we can go to (i+1,j) or (i,j+1)
        for i in range(m-2, -1, -1):
            # To enter (i, n-1), after taking dungeon[i][n-1], 
            # we need to have enough HP to enter (i+1, n-1)
            # HP_before + dungeon[i][n-1] >= dp[i+1][n-1]
            # HP_before >= dp[i+1][n-1] - dungeon[i][n-1]
            # But HP_before must be at least 1
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        # Fill last row (can only go right)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        # Fill the rest of the table
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # We can go either right or down from (i,j)
                # Choose the path that requires minimum initial HP
                # After entering (i,j) and applying dungeon[i][j], we need enough
                # HP to enter either (i+1,j) or (i,j+1)
                min_hp_on_exit = min(dp[i+1][j], dp[i][j+1])
                
                # Before applying dungeon[i][j], we need:
                # current_hp + dungeon[i][j] >= min_hp_on_exit
                # current_hp >= min_hp_on_exit - dungeon[i][j]
                # But current_hp must be at least 1
                dp[i][j] = max(1, min_hp_on_exit - dungeon[i][j])
        
        return dp[0][0]