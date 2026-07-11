class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate area of each rectangle independently
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Find the overlapping rectangle coordinates
        # Overlap exists only if rectangles intersect in both x and y dimensions
        # For x-axis: overlap is from max(left edges) to min(right edges)
        overlap_x1 = max(ax1, bx1)
        overlap_x2 = min(ax2, bx2)
        
        # For y-axis: overlap is from max(bottom edges) to min(top edges)
        overlap_y1 = max(ay1, by1)
        overlap_y2 = min(ay2, by2)
        
        # Calculate overlap area
        # If there's no overlap, one or both dimensions will be non-positive
        overlap_width = max(0, overlap_x2 - overlap_x1)
        overlap_height = max(0, overlap_y2 - overlap_y1)
        overlap_area = overlap_width * overlap_height
        
        # Total area = sum of both areas minus the overlap (to avoid double counting)
        return area_a + area_b - overlap_area