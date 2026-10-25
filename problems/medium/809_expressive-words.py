class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        # Helper: convert a string into a list of (character, count) groups.
        def group_counts(t: str):
            if not t:
                return []
            groups = []
            i = 0
            n = len(t)
            while i < n:
                c = t[i]
                j = i
                # Expand to the end of the consecutive block of c.
                while j < n and t[j] == c:
                    j += 1
                groups.append((c, j - i))
                i = j
            return groups

        # Pre‑compute groups for the target string s.
        s_groups = group_counts(s)
        ans = 0

        for w in words:
            w_groups = group_counts(w)
            # Different number of groups → impossible to match.
            if len(w_groups) != len(s_groups):
                continue

            ok = True
            for (c1, cnt1), (c2, cnt2) in zip(w_groups, s_groups):
                # Characters must be identical.
                if c1 != c2:
                    ok = False
                    break
                # Cannot shrink a group.
                if cnt1 > cnt2:
                    ok = False
                    break
                # If we need to extend (cnt1 < cnt2), the final length must be at least 3.
                if cnt1 < cnt2 and cnt2 < 3:
                    ok = False
                    break
            if ok:
                ans += 1

        return ans