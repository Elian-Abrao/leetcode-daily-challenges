class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Track net displacement in x and y axes.
        x = 0
        y = 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            # Input constraint guarantees only these four characters.

        # Returns to origin only if both coordinates are zero.
        return x == 0 and y == 0