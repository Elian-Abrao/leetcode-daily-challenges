from collections import defaultdict

class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        # ---------- pre‑compute masks for numbers 1..30 ----------
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]      # 10 primes ≤ 30
        mask_for = [None] * 31        # None = not square‑free
        mask_for[1] = 0               # 1 contributes no primes

        for v in range(2, 31):
            x = v
            mask = 0
            ok = True
            for i, p in enumerate(primes):
                if x % p == 0:
                    cnt = 0
                    while x % p == 0:
                        x //= p
                        cnt += 1
                    if cnt > 1:          # prime squared → invalid
                        ok = False
                        break
                    mask |= (1 << i)      # set the bit for this prime
            if ok and x == 1:            # completely factorised
                mask_for[v] = mask
            # else leave as None (e.g. 4, 8, 9, 12, …)

        # ---------- count frequencies ----------
        freq = [0] * 31
        for val in nums:
            freq[val] += 1

        cnt1 = freq[1]                   # how many 1's are present

        # ---------- group square‑free numbers (>1) by their mask ----------
        mask_cnt = defaultdict(int)      # mask → total multiplicity
        for v in range(2, 31):
            if freq[v] and mask_for[v] is not None and mask_for[v] != 0:
                mask_cnt[mask_for[v]] += freq[v]

        # ---------- DP over the 10‑bit prime space ----------
        FULL_MASK = 1 << 10
        dp = [0] * FULL_MASK
        dp[0] = 1

        for m, ways in mask_cnt.items():
            # 'not take' case is already present in the copy
            new_dp = dp[:]
            for state in range(FULL_MASK):
                if state & m == 0:                # no overlapping primes
                    new_state = state | m
                    new_dp[new_state] = (new_dp[new_state] + dp[state] * ways) % MOD
            dp = new_dp

        # ---------- sum over all non‑empty masks ----------
        total = 0
        for state in range(1, FULL_MASK):
            total = (total + dp[state]) % MOD

        # ---------- incorporate arbitrary subsets of 1's ----------
        total = total * pow(2, cnt1, MOD) % MOD
        return total