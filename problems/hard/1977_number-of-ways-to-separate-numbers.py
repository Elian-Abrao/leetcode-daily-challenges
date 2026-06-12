class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        
        if num[0] == '0':
            return 0
        
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
                else:
                    lcp[i][j] = 0
        
        def compare(i, length, j):
            common = lcp[i][j]
            if common >= length:
                return True
            return num[i + common] >= num[j + common]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for length in range(1, n + 1):
            if num[0] != '0':
                dp[length][length] = 1
        
        for i in range(2, n + 1):
            for prev_len in range(1, i):
                prev_start = i - prev_len
                
                if num[prev_start] == '0':
                    continue
                
                for prev_prev_len in range(1, prev_start + 1):
                    prev_prev_start = prev_start - prev_prev_len
                    
                    if dp[prev_start][prev_prev_len] == 0:
                        continue
                    
                    if num[prev_prev_start] == '0':
                        continue
                    
                    if prev_len > prev_prev_len:
                        dp[i][prev_len] = (dp[i][prev_len] + dp[prev_start][prev_prev_len]) % MOD
                    elif prev_len == prev_prev_len:
                        if compare(prev_start, prev_len, prev_prev_start):
                            dp[i][prev_len] = (dp[i][prev_len] + dp[prev_start][prev_prev_len]) % MOD
        
        result = sum(dp[n]) % MOD
        return result