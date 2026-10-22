class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        """
        Simulates dropping squares one by one on the x-axis.
        For each square, we determine its landing height by checking all
        previously placed squares that it overlaps horizontally (strict overlap).
        The square lands on top of the highest such square (or on the ground).
        After each drop, we record the overall maximum height among all squares.
        """
        n = len(positions)
        # heights[i] = top y-coordinate of the i-th square after it lands
        heights = [0] * n
        ans = []
        current_max = 0

        for i, (left, side) in enumerate(positions):
            right = left + side
            bottom = 0  # starting y for the falling square

            # Check all previously placed squares to find the highest one
            # that overlaps the current square in the x‑projection.
            for j in range(i):
                prev_left, prev_side = positions[j]
                prev_right = prev_left + prev_side

                # Overlap condition: intervals must intersect with positive length.
                # Left edges must be strictly less than the opposite right edges.
                if left < prev_right and prev_left < right:
                    # The current square will land on top of square j if it is the highest.
                    bottom = max(bottom, heights[j])

            # Current square's top y-coordinate after landing
            heights[i] = bottom + side
            # Update the global tallest stack height
            if heights[i] > current_max:
                current_max = heights[i]
            ans.append(current_max)

        return ans