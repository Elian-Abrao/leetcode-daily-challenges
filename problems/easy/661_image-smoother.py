class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                total = 0
                count = 0

                # Inspect all cells in the 3x3 block centered at (row, col)
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = row + dr, col + dc

                        # Only include cells inside the image boundaries
                        if 0 <= nr < m and 0 <= nc < n:
                            total += img[nr][nc]
                            count += 1

                result[row][col] = total // count

        return result