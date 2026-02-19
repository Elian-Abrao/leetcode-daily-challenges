class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # Provavelmente a solução mais simples, porém não é a mais eficiente
        # muito provavelmente eh possivel atimizar e atingir O(n) porem nao consegui pensar em uma solucao
        # A minha solucao ja atinge O(n*m) porem nao eh a mais eficiente
        counts = 0
        while word * (counts + 1) in sequence:
            counts += 1
        return counts

solution = Solution()
print(solution.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")) # 2
print(solution.optimized_maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")) # 2