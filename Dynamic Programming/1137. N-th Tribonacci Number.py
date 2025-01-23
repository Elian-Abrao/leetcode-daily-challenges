class Solution:
    def tribonacci(self, n: int) -> int:
        # Casos base
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Variáveis para armazenar os três últimos valores da sequência
        t0, t1, t2 = 0, 1, 1

        # Calculando iterativamente até o n-ésimo número
        for _ in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next

        return t2


solution = Solution()

n = 25
print(solution.tribonacci(n)) # 4