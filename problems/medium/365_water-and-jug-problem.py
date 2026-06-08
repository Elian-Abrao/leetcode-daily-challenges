from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Edge case: if target is larger than total capacity, impossible
        if target > x + y:
            return False
        
        # Edge case: if target is 0, we can always achieve it (empty both jugs)
        if target == 0:
            return True
        
        # Edge case: if either jug is 0, we can only measure multiples of the other
        if x == 0:
            return target == y
        if y == 0:
            return target == x
        
        # Mathematical insight (Bezout's identity):
        # We can measure any amount of the form a*x + b*y where a, b are integers
        # (positive for filling, negative for emptying conceptually).
        # The set of all such amounts is exactly the multiples of gcd(x, y).
        # 
        # Therefore, we can achieve 'target' if and only if:
        # 1. target <= x + y (not exceeding total capacity)
        # 2. target is a multiple of gcd(x, y)
        
        g = gcd(x, y)
        
        # Check if target is divisible by gcd(x, y)
        return target % g == 0