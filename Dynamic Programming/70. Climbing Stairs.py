class Solution:
    def climbStairs(self, n: int) -> int:
        step_even, step_odd = 0, 1

        # Casos base: 1 ou 2 degraus
        if n < 3:
            return n

        for step in range(1, n+1):
            if (step % 2) == 0:
                step_even = step_even + step_odd
                # print(f"{step} -> {step_odd} + {step_even} = {step_even}")

            else:
                step_odd = step_even + step_odd
                # print(f"{step} -> {step_even} + {step_odd} = {step_odd}")

        output = step_even + step_odd
        return output
    
    # Ambas solucoes atigem O(n) porem dessa forma facilita em nao necessitar a validacao de par ou impar
    def optimized_climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        prev1, prev2 = 1, 2  # Iniciando direto nos degraus 1 e 2

        for _ in range(3, n + 1):  # Comecando no terceiro degrau
            curr = prev1 + prev2  # Maneiras de chegar ao degrau atual
            prev1, prev2 = prev2, curr  # Atualize os valores

        return prev2  # O último valor é o número total de maneiras
            


solution = Solution()
n = 5
print(solution.climbStairs(n))
print(solution.optimized_climbStairs(n))