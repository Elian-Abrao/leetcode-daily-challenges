from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression keeps repeated connectivity checks near-constant.
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        # Union by size keeps trees shallow.
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        dsu = DSU(n)

        masks = []
        mask_to_index = {}

        for index, word in enumerate(words):
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)

            # Equal masks are trivially connected via "replace with itself".
            if mask in mask_to_index:
                dsu.union(index, mask_to_index[mask])
            else:
                mask_to_index[mask] = index

        deleted_mask_owner = {}

        for index, mask in enumerate(masks):
            current = dsu.find(index)

            # Deleting one letter connects to any existing word with that smaller mask.
            # The same deleted mask also links replacement neighbors together.
            for bit in range(26):
                if (mask >> bit) & 1 == 0:
                    continue

                removed = mask ^ (1 << bit)

                if removed in mask_to_index:
                    dsu.union(current, mask_to_index[removed])
                    current = dsu.find(current)

                if removed in deleted_mask_owner:
                    dsu.union(current, deleted_mask_owner[removed])
                    current = dsu.find(current)
                else:
                    deleted_mask_owner[removed] = current

        group_count = 0
        largest_group = 0

        for index in range(n):
            if dsu.find(index) == index:
                group_count += 1
                largest_group = max(largest_group, dsu.size[index])

        return [group_count, largest_group]