class Solution:
    # Solucao de forca bruta com Complexidade exponencial de 2 elevado a n
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return (self.fib(n-1) + self.fib(n-2))
    
    # dessa forma conseguimos otimizar para O(n)
    def optimized_fib(self, n: int) -> int:
        if n < 2:
            return n

        a, b = 0, 1  # F(0) e F(1)
        for _ in range(2, n + 1):
            a, b = b, a + b  # Atualizando os dois ultimos valores

        return b  # Retorna F(n)

solution = Solution()
n = 30
print(solution.fib(n))
print(solution.optimized_fib(n))