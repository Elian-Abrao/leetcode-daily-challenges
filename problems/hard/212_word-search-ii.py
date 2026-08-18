from __future__ import annotations
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # ------------------------------------------------------------
        # Build a Trie from the given list of words.
        # Each node has:
        #   - children: dict mapping character -> TrieNode
        #   - word:     stores the full word if this node is the end of a word
        # ------------------------------------------------------------
        class TrieNode:
            __slots__ = ('children', 'word')
            def __init__(self):
                self.children = {}
                self.word = None      # None means not a terminal node

        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w            # store the complete word at the terminal node

        # ------------------------------------------------------------
        # Depth-first search on the board, guided by the Trie.
        # We reuse the board cell to mark visited temporarily by storing '#'
        # to avoid extra visited structure.
        # ------------------------------------------------------------
        m, n = len(board), len(board[0])
        res = []

        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int, node: TrieNode) -> None:
            """Search from cell (r,c) with current Trie node."""
            ch = board[r][c]
            # If the character is not in the current node's children, stop.
            next_node = node.children.get(ch)
            if next_node is None:
                return

            # If we reached the end of a word, record it and mark the node
            # so we don't add the same word twice (set word to None).
            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None   # avoid duplicates

            # Mark current cell as visited by overwriting temporarily
            board[r][c] = '#'

            # Explore neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # Restore the original character after backtracking
            board[r][c] = ch

        # ------------------------------------------------------------
        # Start DFS from every cell.
        # ------------------------------------------------------------
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res