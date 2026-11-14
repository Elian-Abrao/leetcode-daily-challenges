class TrieNode:
    __slots__ = ('children', 'sum')
    def __init__(self):
        self.children = {}
        self.sum = 0


class MapSum:
    """MapSum that supports prefix sum queries using a trie."""

    def __init__(self):
        self.root = TrieNode()
        # keep track of current value for each key to compute delta on reinsert
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        """Insert a key-value pair. If key already exists, override it."""
        delta = val - self.values.get(key, 0)
        # Nothing to update if the value hasn't changed
        if delta == 0:
            return

        node = self.root
        # root.sum represents the sum of all keys (empty prefix)
        node.sum += delta
        # traverse the key, creating nodes if necessary
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # every node on the path accumulates the delta
            node.sum += delta

        # store the new value for this key
        self.values[key] = val

    def sum(self, prefix: str) -> int:
        """Return the sum of all values whose keys start with the given prefix."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        # node.sum holds the total sum for all keys that have this prefix
        return node.sum