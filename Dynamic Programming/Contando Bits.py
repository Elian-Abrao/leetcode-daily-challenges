class Solution:
    # Essa minha solucao ja eh funcional e atinge O(n log n)
    def countBits_log_n(self, n: int) -> list[int]:
        resp = []
        for i in range(n+1):
            soma = bin(i).count('1')
            resp.append(soma)
        return resp

    def countBits(self, n: int) -> list[int]:
        # Array dp para armazenar o número de bits 1 para cada número de 0 até n
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Reaproveitamos a contagem de bits de i // 2 (ou seja, o número sem o último bit)
            # porque deslocar para a direita remove o último bit, que já foi computado.
            # Somamos 1 se o último bit de i for 1, pois isso adiciona um novo bit 1 ao número.
            dp[i] = dp[i >> 1] + (i & 1)

        return dp

solution = Solution()
n = 10
print(solution.countBits(n))