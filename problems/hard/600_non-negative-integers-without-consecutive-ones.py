class Solution:
    def findIntegers(self, n: int) -> int:
        bits = bin(n)[2:]
        L = len(bits)
        fib = [0] * (L + 2)
        fib[0] = 1
        fib[1] = 2
        for i in range(2, L + 2):
            fib[i] = fib[i-1] + fib[i-2]
        ans = 0
        has_consecutive = False
        for i, ch in enumerate(bits):
            if ch == '1':
                ans += fib[L - i - 1]
                if i > 0 and bits[i-1] == '1':
                    has_consecutive = True
                    break
        if not has_consecutive:
            ans += 1
        return ans