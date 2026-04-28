import random
import math
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        # Store circle parameters for use in randPoint
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate uniform random point inside circle using polar coordinates
        # Key insight: naive approach of uniform angle + uniform radius is WRONG
        # because it over-samples points near the center (density increases toward center)
        
        # Correct approach: use sqrt to adjust radial distribution
        # PDF for radius: P(r) = 2r/R^2 for uniform area distribution
        # CDF: F(r) = r^2/R^2
        # Inverse CDF: r = R * sqrt(u) where u ~ Uniform(0,1)
        
        # Generate random angle uniformly in [0, 2π)
        angle = random.uniform(0, 2 * math.pi)
        
        # Generate random radius with correct distribution (sqrt for uniform area)
        # This ensures points are uniformly distributed by AREA, not by radius
        r = self.radius * math.sqrt(random.random())
        
        # Convert polar coordinates (r, angle) to Cartesian (x, y)
        x = self.x_center + r * math.cos(angle)
        y = self.y_center + r * math.sin(angle)
        
        return [x, y]