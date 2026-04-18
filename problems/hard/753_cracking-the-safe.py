class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # De Bruijn sequence construction using the FKM algorithm
        a = [0] * (n + 1)  # 1-based indexing up to n
        sequence = []

        def db(t: int, p: int):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p + 1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)

        db(1, 1)

        # Convert digits to string
        digits = ''.join(chr(ord('0') + d) for d in sequence)

        # Append first n-1 digits to linearize the cyclic sequence
        if n > 1:
            digits += ''.join(chr(ord('0') + sequence[i]) for i in range(n - 1))

        return digits