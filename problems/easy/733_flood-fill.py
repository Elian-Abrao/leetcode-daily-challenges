class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # If the starting pixel already has the target color, no work needed.
        original_color = image[sr][sc]
        if original_color == color:
            return image

        rows, cols = len(image), len(image[0])
        # Use a stack for iterative DFS to avoid recursion depth issues.
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            # Only process cells that still have the original color.
            if image[r][c] != original_color:
                continue
            # Change to the new color.
            image[r][c] = color
            # Explore four cardinal directions.
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    stack.append((nr, nc))
        return image