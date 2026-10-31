class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        # (power^k) % modulo
        pow_k = pow(power, k, modulo)

        # last possible starting index of a length‑k substring
        last_start = n - k

        # ------------------------------------------------------------
        # 1) compute the hash of the last window (rightmost substring)
        #    using Horner's method from right to left:
        #        h = ( ... (val(last)*p + val(second-last))*p + ... )
        #    This yields exactly the required polynomial.
        # ------------------------------------------------------------
        h = 0
        # traverse indices from n-1 down to last_start
        for pos in range(last_start + k - 1, last_start - 1, -1):
            h = (h * power + (ord(s[pos]) - 96)) % modulo

        # initialise best starting index
        best = last_start if h == hashValue else -1

        # hash for the window starting at i+1 (initially the last window)
        next_hash = h

        # ------------------------------------------------------------
        # 2) slide backwards using the exact recurrence:
        #        H_i = val_i + p * H_{i+1} - val_{i+k} * p^k   (mod modulo)
        #    The identity holds as integers, therefore also modulo.
        #    This avoids division by p and works for any modulo.
        # ------------------------------------------------------------
        for i in range(last_start - 1, -1, -1):
            val_i = ord(s[i]) - 96
            val_ik = ord(s[i + k]) - 96
            cur_hash = (val_i + power * next_hash - val_ik * pow_k) % modulo
            if cur_hash == hashValue:
                best = i          # smaller index, so update
            next_hash = cur_hash

        # problem guarantees that a valid substring exists
        return s[best:best + k]