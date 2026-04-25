class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        
        max_m = num.bit_length()
        
        for m in range(max_m, 1, -1):
            left = 2
            right = int(num ** (1.0 / (m - 1))) + 1
            
            while left <= right:
                k = (left + right) // 2
                
                total = 0
                power = 1
                for _ in range(m):
                    total += power
                    power *= k
                
                if total == num:
                    return str(k)
                elif total < num:
                    left = k + 1
                else:
                    right = k - 1
        
        return str(num - 1)