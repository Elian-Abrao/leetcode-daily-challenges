from __future__ import annotations

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # ---------- Disjoint Set Union (Union-Find) ----------
        class DSU:
            """Iterative path compression + union by rank."""
            def __init__(self, n: int) -> None:
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x: int) -> int:
                # Path compression (iterative to avoid recursion depth)
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, a: int, b: int) -> None:
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return
                # Union by rank: attach smaller tree under larger tree
                if self.rank[ra] < self.rank[rb]:
                    self.parent[ra] = rb
                elif self.rank[ra] > self.rank[rb]:
                    self.parent[rb] = ra
                else:
                    self.parent[rb] = ra
                    self.rank[ra] += 1

        # ---------- Step 1 : assign unique integer IDs to every email ----------
        email_to_id: dict[str, int] = {}
        email_to_name: dict[str, str] = {}   # name associated with the email (any account)
        id_counter = 0

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    email_to_name[email] = name
                    id_counter += 1

        # ---------- Step 2 : union all emails inside each account ----------
        dsu = DSU(id_counter)

        for account in accounts:
            emails = account[1:]          # all emails of this account
            if not emails:
                continue
            first_id = email_to_id[emails[0]]
            for email in emails[1:]:
                dsu.union(first_id, email_to_id[email])

        # ---------- Step 3 : group emails by their DSU component ----------
        root_to_emails: dict[int, list[str]] = {}
        for email, eid in email_to_id.items():
            root = dsu.find(eid)
            root_to_emails.setdefault(root, []).append(email)

        # ---------- Step 4 : build the final answer ----------
        result: list[list[str]] = []
        for emails in root_to_emails.values():
            name = email_to_name[emails[0]]   # all emails in this group belong to the same person
            emails.sort()                     # alphabetical order (lexicographic)
            result.append([name] + emails)

        return result