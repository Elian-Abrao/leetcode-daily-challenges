from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # This is a convex hull problem (Jarvis/Graham scan or monotone chain)
        # We use Andrew's Monotone Chain algorithm which is efficient and handles collinear points well
        
        # Edge case: if we have 3 or fewer points, all are on the hull
        if len(trees) <= 3:
            return trees
        
        def cross_product(o, a, b):
            # Calculate cross product of vectors OA and OB
            # Positive: counter-clockwise turn
            # Negative: clockwise turn
            # Zero: collinear
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        # Sort points lexicographically (first by x, then by y)
        points = sorted(trees)
        
        # Build lower hull
        lower = []
        for p in points:
            # Remove points that would create a clockwise turn
            # Keep collinear points by using < instead of <=
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        # Build upper hull
        upper = []
        for p in reversed(points):
            # Remove points that would create a clockwise turn
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Remove last point of each half because it's repeated at the beginning of the other half
        # Combine both hulls
        # Note: lower[:-1] + upper[:-1] would normally work, but we need to handle collinear points
        
        # For the fence problem, we need ALL points on the perimeter including collinear ones
        # The above approach might miss some collinear points on the edges
        
        # Better approach: Use monotone chain but keep collinear points
        lower = []
        for p in points:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Combine and remove duplicates
        # lower[-1] == upper[-1] (rightmost point) and lower[0] == upper[0] (leftmost point)
        result = lower[:-1] + upper[:-1]
        
        # However, we still might miss collinear points. Let's use a different approach:
        # After getting the hull, we need to add back collinear points on hull edges
        
        # Re-implement with proper collinear handling
        lower = []
        for p in points:
            # Use < to keep collinear points (not <=)
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Remove duplicates at endpoints and combine
        # Use set to remove duplicates since a point might appear in both hulls
        hull_set = set(map(tuple, lower[:-1] + upper[:-1]))
        
        return [list(p) for p in hull_set]