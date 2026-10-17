class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp0: number of ways for the current row ending with a "two-colour" pattern (e.g., ABA)
        # dp1: number of ways for the current row ending with a "three-colour" pattern (e.g., ABC)
        dp0 = 6  # 6 patterns of type ABA using 3 colours
        dp1 = 6  # 6 patterns of type ABC using 3 colours
        
        for _ in range(1, n):
            # Transition counts derived from combinatorial analysis:
            # from a two-colour pattern: 3 two-colour + 2 three-colour next rows
            # from a three-colour pattern: 2 two-colour + 2 three-colour next rows
            new_dp0 = (dp0 * 3 + dp1 * 2) % MOD
            new_dp1 = (dp0 * 2 + dp1 * 2) % MOD
            dp0, dp1 = new_dp0, new_dp1
        
        return (dp0 + dp1) % MOD