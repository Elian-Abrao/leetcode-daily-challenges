from __future__ import annotations
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        # Recursively build the quad tree by dividing the grid into 4 quadrants
        # Base case: if all cells in current region have same value, create leaf node
        return self._build(grid, 0, 0, len(grid))
    
    def _build(self, grid: List[List[int]], row: int, col: int, size: int) -> Node:
        # Check if current grid region is uniform (all 0s or all 1s)
        if self._is_uniform(grid, row, col, size):
            # Create leaf node with the uniform value
            return Node(
                val=grid[row][col] == 1,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None
            )
        
        # Grid is not uniform, divide into 4 quadrants
        half = size // 2
        
        # Recursively construct each quadrant
        # TopLeft: (row, col) with size half
        top_left = self._build(grid, row, col, half)
        
        # TopRight: (row, col + half) with size half
        top_right = self._build(grid, row, col + half, half)
        
        # BottomLeft: (row + half, col) with size half
        bottom_left = self._build(grid, row + half, col, half)
        
        # BottomRight: (row + half, col + half) with size half
        bottom_right = self._build(grid, row + half, col + half, half)
        
        # Create internal node (val can be any value when isLeaf=False)
        return Node(
            val=True,  # Arbitrary value for internal nodes
            isLeaf=False,
            topLeft=top_left,
            topRight=top_right,
            bottomLeft=bottom_left,
            bottomRight=bottom_right
        )
    
    def _is_uniform(self, grid: List[List[int]], row: int, col: int, size: int) -> bool:
        # Check if all cells in the region [row:row+size, col:col+size] have the same value
        first_val = grid[row][col]
        
        # Scan all cells in the region
        for i in range(row, row + size):
            for j in range(col, col + size):
                if grid[i][j] != first_val:
                    return False
        
        return True