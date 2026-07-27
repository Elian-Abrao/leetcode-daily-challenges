from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Edge case: single element triangle
        if len(triangle) == 1:
            return triangle[0][0]
        
        # Bottom-up DP approach with O(n) space optimization
        # We maintain a 1D array representing the minimum path sum to each position
        # in the current row, updating it as we move up the triangle
        
        n = len(triangle)
        
        # Initialize dp array with the last row of the triangle
        # dp[j] represents the minimum path sum from bottom to position j in current row
        dp = triangle[-1][:]
        
        # Process rows from second-to-last up to the top
        # For each position, we can only come from two positions in the row below:
        # position j or position j+1
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Current cell value + minimum of two possible paths from row below
                # Adjacent positions in next row are col and col+1
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        # After processing all rows, dp[0] contains minimum path from top to bottom
        return dp[0]