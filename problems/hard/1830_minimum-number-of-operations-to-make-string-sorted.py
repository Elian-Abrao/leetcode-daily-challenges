class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)

        # ---------- precompute factorials and inverse factorials ----------
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)          # Fermat inverse
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        # -----------------------------------------------------------------

        # frequency of each letter (0 = 'a', ... 25 = 'z')
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        ans = 0

        for i, ch in enumerate(s):
            c = ord(ch) - 97                # current character as index 0..25
            remaining = n - i - 1           # length of suffix after fixing s[i]

            # denominator product for the current multiset (before fixing s[i])
            base_denom = 1
            for f in freq:
                base_denom = base_denom * inv_fact[f] % MOD

            # Count permutations starting with a smaller character
            for d in range(c):
                if freq[d] == 0:
                    continue
                # new frequency after using d as prefix
                new_freq_d = freq[d] - 1
                # adjust denominator: remove inv_fact[freq[d]], add inv_fact[new_freq_d]
                denom_d = base_denom * fact[freq[d]] % MOD * inv_fact[new_freq_d] % MOD
                # number of permutations for the remaining positions
                cnt = fact[remaining] * denom_d % MOD
                ans = (ans + cnt) % MOD

            # Now fix the actual character: decrease its frequency
            freq[c] -= 1

        return ans