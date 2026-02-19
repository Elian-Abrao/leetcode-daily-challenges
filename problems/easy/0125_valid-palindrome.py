class Solution:
    def longestPalindrome(self, s):
        maior_palindromo = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        # preenchendo a diagonal com 1
        for i in range(len(s)):
            dp[i][i] = True
            maior_palindromo = s[i]
            
        # preenchendo a tabela dp
        for i in range(len(s)-1, -1, -1):
            # j começa da posição i: para trabalhar apenas na parte superior da diagonal
            for j in range(i+1, len(s)):  
                if s[i] == s[j]:  # se os caracteres coincidem
                    # se o comprimento da sub_string cortada for apenas uma letra e os caracteres forem iguais, podemos dizer que são palíndromos dp[i][j] = True
                    # se a sub_string cortada for maior que 1, então devemos verificar se a string interna também é um palíndromo (verificar se dp[i+1][j-1] é True)
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # também precisamos acompanhar a sequência máxima de palíndromos
                        if len(maior_palindromo) < len(s[i:j+1]):
                            maior_palindromo = s[i:j+1]
                
        return maior_palindromo

Solution = Solution()
print(Solution.longestPalindrome(s="rabcbaabcbdskhjfbsdfsjdbflsdfniksdnlfksnmdkfnsldjnfjklskkkgfdklshghkjlsfdhgkjlfdsghjkfsdlhgjkfdls;ghfsdljk;gfsdhljk;gfehjl;gfsdhjkl;hfjkg;dsgfsdjhk;gfdshjk;fghujkd;hjksgfdhjklgsdfhjklsgdfsghdjklfdfghjklgfdhjlksghjkdflshgjkfdlshjksdglfhkldjgflkjhgfdsasdfghjkllkjhgfdskkkkkdbnfksjenbksbefkslejfblskjhbdfkbsbuuuuduksjkjjjjdjdkslkdksfacar"))
