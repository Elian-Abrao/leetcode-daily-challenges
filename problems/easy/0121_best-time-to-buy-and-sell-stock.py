class Solution:
    # Solucao O(n²)
    def maxProfit_Solucao_Ineficiente(self, prices: list[int]) -> int:
        lucro = 0

        for i in range(len(prices)-1):
            for j in (prices[i+1:]):
                if (j - prices[i]) > lucro:
                    lucro = (j - prices[i])
                    print(f"{j} - {prices[i]} = {lucro}")
        return lucro
    
    def maxProfit(self, prices: list[int]) -> int:
        # Essa funcao funciona como O(n) pois passamos uma unica vez pelo array, visto, que nao comparamos o atual com os proximos, mas sim, vamos comparando as diferencas, entre o menor valor encontrado ate o momento, e o valor atual
        min_price = float('inf')  # Inicializa com infinito
        max_profit = 0  # Lucro máximo inicial

        for valor in prices:
            if valor < min_price: # Se o valor atual for menor que o menor preco, guardamos ele
                min_price = valor  # Atualiza o menor preço

            elif valor - min_price > max_profit: # caso ele nao seja menor que o atual, verificamos se possue a menor diferenca
                max_profit = valor - min_price  # Calcula o lucro máximo
            
        return max_profit

    

solution = Solution()
prices = [9,8,7,10,1,2,3,4,5,6]
print(solution.maxProfit(prices))
        