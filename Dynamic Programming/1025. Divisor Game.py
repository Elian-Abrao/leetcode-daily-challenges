class Solution:
    def divisorGame(self, n: int) -> bool:
        # Cria um array dp para armazenar os resultados
        dp = [False] * (n + 1)
        
        # Base case: se n = 2, Alice sempre ganha
        if n >= 2:
            dp[2] = True

        # Preenche o dp para todos os valores de 3 até n
        for i in range(3, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        
        return dp[n]

# Exemplos de teste
solution = Solution()
print(solution.divisorGame(2))  # Saída: True
print(solution.divisorGame(3))  # Saída: False
