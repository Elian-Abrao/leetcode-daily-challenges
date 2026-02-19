class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangulo_pascal = []
        triangulo_pascal.append([1])
        for i in range(numRows-1): 
            novaLinha = [1]
            for j in range(i):
                novaLinha.append(triangulo_pascal[i][j] + triangulo_pascal[i][j+1])
            novaLinha.append(1)
            triangulo_pascal.append(novaLinha)
        return triangulo_pascal

solutino = Solution()
print(solutino.generate(5)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]