class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        if n ==2:
            return min(cost[0], cost[1])
        
        # Array para armazenar os custos acumulados, inicializando em 0
        array = [0] * n
        print(array)
        array[0], array[1] = cost[0], cost[1]

        # Preenchendo o array dp com os custos acumulados
        for i in range(2, n):
            array[i] = cost[i] + min(array[i-1], array[i-2])

        # Retorna o custo mínimo para alcançar o topo
        return min(array[n-1], array[n-2])

solution = Solution()
cost = [ 1 ,100, 1 ,1, 1 ,100, 1 , 1 ,100, 1 ]
print(solution.minCostClimbingStairs(cost)) # 15
