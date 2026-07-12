from typing import List
import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_sums = []
        cumulative = 0
        
        # Build prefix sum array where each entry represents cumulative count of integer points
        # up to and including rectangle i
        for a, b, x, y in rects:
            # Count of integer points in rectangle: (width + 1) * (height + 1)
            # Both boundaries are inclusive, so we add 1 to each dimension
            num_points = (x - a + 1) * (y - b + 1)
            cumulative += num_points
            self.prefix_sums.append(cumulative)
        
        self.total_points = cumulative

    def pick(self) -> List[int]:
        # Choose a random point index from [0, total_points)
        # This ensures uniform distribution across all integer points
        target = random.randint(1, self.total_points)
        
        # Binary search to find which rectangle contains this point
        # bisect_left finds the leftmost position where target <= prefix_sums[i]
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        
        # If target equals a prefix sum exactly, we're at the boundary
        # Need to move to the next rectangle that actually contains this point index
        if rect_idx < len(self.prefix_sums) and self.prefix_sums[rect_idx] < target:
            rect_idx += 1
        
        # Get the selected rectangle
        a, b, x, y = self.rects[rect_idx]
        
        # Calculate how many points are in rectangles before this one
        points_before = self.prefix_sums[rect_idx - 1] if rect_idx > 0 else 0
        
        # Local index within the current rectangle (0-indexed)
        local_idx = target - points_before - 1
        
        # Width of the rectangle (number of columns)
        width = x - a + 1
        
        # Convert 1D local index to 2D coordinates
        # Row-major order: point at (dx, dy) has index dy * width + dx
        row = local_idx // width
        col = local_idx % width
        
        # Map back to actual coordinates
        return [a + col, b + row]