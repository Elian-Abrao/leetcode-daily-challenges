class Solution:
    def twoSum(self, nums, target):
        # Criando um hash_map para acelerar a busca, pois o tempo de busca em um dicionario é O(1)
        hash_map = {}

        # loop para interar todos os elementos
        for i in range(len(nums)):
            # Calculando o valor que falta para completar o target
            complement = target - nums[i]

            # Verificando se o complemento esta no hash_map
            if complement in hash_map:
                # Se estiver, retornamos a posicao do complemento e a posicao atual
                return [hash_map[complement], i]
            # Se nao estiver, adicionamos o valor no hash_map
            hash_map[nums[i]] = i

nums = [3, 2, 4, 5, 7, 9, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))