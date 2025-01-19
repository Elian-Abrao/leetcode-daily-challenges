class Solution:
    def getRow(self, rowIndex: int) -> list[list[int]]:
        triangulo_pascal = []
        triangulo_pascal.append([1])
        for i in range(rowIndex): 
            novaLinha = [1]
            for j in range(i):
                novaLinha.append(triangulo_pascal[i][j] + triangulo_pascal[i][j+1])
            novaLinha.append(1)
            triangulo_pascal.append(novaLinha)
        return triangulo_pascal[rowIndex]

solutino = Solution()
print(solutino.getRow(3)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]