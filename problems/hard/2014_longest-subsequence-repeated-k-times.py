class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)

        # --- Step 1: character frequency ---
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        # --- Step 2: candidate characters (appear at least k times), sorted descending ---
        cand = []
        for i in range(25, -1, -1):          # from 'z' down to 'a'
            if freq[i] >= k:
                cand.append(chr(97 + i))
        if not cand:
            return ""

        # --- Step 3: maximum possible length of the answer ---
        Lmax = n // k                    # always < 8 because n < k * 8

        # --- Step 4: precompute next occurrence table ---
        # nxt[pos][c] = smallest index >= pos where s[index] == c, or n if none
        nxt = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            row = nxt[i]
            nxt_row_next = nxt[i + 1]
            # copy next row's values
            for c in range(26):
                row[c] = nxt_row_next[c]
            # update for current character
            row[ord(s[i]) - 97] = i

        # --- Step 5: helper to check whether seq repeated k times is a subsequence ---
        def is_valid(seq: str) -> bool:
            """Return True iff seq * k is a subsequence of s."""
            pos = 0
            for _ in range(k):
                for ch in seq:
                    nxt_pos = nxt[pos][ord(ch) - 97]
                    if nxt_pos == n:
                        return False
                    pos = nxt_pos + 1
            return True

        # --- Step 6: DFS to build the longest valid string ---
        best = ""

        def dfs(cur: str) -> None:
            nonlocal best
            # try to extend current valid string by each candidate character
            for c in cand:
                nxt_str = cur + c
                if len(nxt_str) > Lmax:
                    continue
                if is_valid(nxt_str):
                    if len(nxt_str) > len(best) or (len(nxt_str) == len(best) and nxt_str > best):
                        best = nxt_str
                    dfs(nxt_str)

        dfs("")
        return best