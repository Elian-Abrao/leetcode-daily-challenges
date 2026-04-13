class Solution:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['_end_'] = True

    def search(self, word: str) -> bool:
        def dfs(pos: int, node: dict) -> bool:
            if pos == len(word):
                return '_end_' in node

            ch = word[pos]
            if ch == '.':
                for key, child in node.items():
                    if key == '_end_':
                        continue
                    if dfs(pos + 1, child):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(pos + 1, node[ch])

        return dfs(0, self.root)