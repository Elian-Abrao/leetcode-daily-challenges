from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge case: empty board or word
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        # Optimization: count character frequencies in board vs word
        # If word requires more of any character than exists in board, return False early
        from collections import Counter
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        for char, count in word_counter.items():
            if board_counter[char] < count:
                return False
        
        # Optimization: start search from the less frequent end of the word
        # This reduces the number of starting positions we need to try
        if word_counter[word[0]] > word_counter[word[-1]]:
            word = word[::-1]
        
        def dfs(row: int, col: int, index: int) -> bool:
            # Successfully matched entire word
            if index == len(word):
                return True
            
            # Boundary checks
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            
            # Character mismatch or cell already visited in current path
            if board[row][col] != word[index]:
                return False
            
            # Mark cell as visited by temporarily modifying it
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore all 4 directions: up, down, left, right
            found = (dfs(row - 1, col, index + 1) or
                     dfs(row + 1, col, index + 1) or
                     dfs(row, col - 1, index + 1) or
                     dfs(row, col + 1, index + 1))
            
            # Restore cell value for other paths (backtrack)
            board[row][col] = temp
            
            return found
        
        # Try starting DFS from each cell that matches the first character
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False