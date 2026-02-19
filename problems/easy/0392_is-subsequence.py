class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current = 0
        result = ''
        for letter in s:
            for i in range(current, len(t)):
                if letter == t[i]:
                    current = i+1
                    result = result + t[i]
                    # print(t[i])
                    break

        if result == s:
            return True
        else: return False

    def optimized_isSubsequence(self, s: str, t: str) -> bool:
        pointer_s, pointer_t = 0, 0  # Ponteiros para ambas as strings
        
        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:  # Letras coincidem
                pointer_s += 1  # Avance em `s`
            pointer_t += 1  # Sempre avance em `t`
        
        # Verifica se conseguimos percorrer toda a string `s`
        return pointer_s == len(s)

solution = Solution()
s, t = 'aza', 'abzba'
s, t = 'abc', 'ahbgdc'
print(solution.isSubsequence(s, t))
print(solution.optimized_isSubsequence(s, t))