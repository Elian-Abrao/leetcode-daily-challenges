class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        
        result = 1
        
        for i in range(1, n + 1):
            ways = i * (2 * i - 1)
            result = (result * ways) % MOD
        
        return result