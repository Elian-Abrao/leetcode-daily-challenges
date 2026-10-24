class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        Count distinct substrings that can be written as a + a.
        Uses double rolling hash to compare halves in O(1) and
        stores a set of (hash1, hash2, length) to guarantee uniqueness.
        """
        n = len(text)
        # Two large primes to make collisions virtually impossible
        MOD1 = 1_000_000_007
        MOD2 = 1_000_000_009
        BASE = 131          # any large prime > alphabet size

        # ---- precompute prefix hashes and powers ----
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        for i, ch in enumerate(text, 1):
            # map 'a'..'z' to 1..26 (avoid leading zero)
            val = ord(ch) - 96
            h1[i] = (h1[i-1] * BASE + val) % MOD1
            h2[i] = (h2[i-1] * BASE + val) % MOD2
            pow1[i] = (pow1[i-1] * BASE) % MOD1
            pow2[i] = (pow2[i-1] * BASE) % MOD2

        # helper to compute hash of substring [l, r)
        def get_hash(l, r, h, pow, mod):
            length = r - l
            return (h[r] - h[l] * pow[length]) % mod

        seen = set()

        # ---- enumerate all possible start positions ----
        for i in range(n):
            # half‑length k: full length = 2k, must not exceed n
            max_k = (n - i) // 2
            for k in range(1, max_k + 1):
                mid = i + k
                right = i + 2 * k

                # ---- compare the two halves using both moduli ----
                # (first modulus)
                first1 = get_hash(i, mid, h1, pow1, MOD1)
                second1 = get_hash(mid, right, h1, pow1, MOD1)
                if first1 != second1:
                    continue
                # (second modulus)
                first2 = get_hash(i, mid, h2, pow2, MOD2)
                second2 = get_hash(mid, right, h2, pow2, MOD2)
                if first2 != second2:
                    continue

                # ---- valid echo substring ----
                full1 = get_hash(i, right, h1, pow1, MOD1)
                full2 = get_hash(i, right, h2, pow2, MOD2)
                # include length to avoid collisions across different lengths
                seen.add((full1, full2, 2 * k))

        return len(seen)