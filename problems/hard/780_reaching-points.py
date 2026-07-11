class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Work backwards from (tx, ty) to (sx, sy) using reverse operations
        # If we have (x, y) where x > y, it came from (x - y, y)
        # If we have (x, y) where y > x, it came from (x, y - x)
        
        # Continue until we either reach (sx, sy) or determine it's impossible
        while tx >= sx and ty >= sy:
            # Base case: we've reached the source point
            if tx == sx and ty == sy:
                return True
            
            # If tx > ty, the last operation must have been (tx - ty, ty) -> (tx, ty)
            # We can reverse multiple steps at once using modulo to avoid TLE
            if tx > ty:
                # If ty == sy, we need tx to be reachable from sx by adding sy repeatedly
                # This means (tx - sx) must be divisible by sy
                if ty == sy:
                    return (tx - sx) % sy == 0
                # Otherwise, reverse as many steps as possible: tx = tx % ty
                # But we need to ensure we don't go below sx
                tx %= ty
            else:  # ty > tx
                # If tx == sx, we need ty to be reachable from sy by adding sx repeatedly
                # This means (ty - sy) must be divisible by sx
                if tx == sx:
                    return (ty - sy) % sx == 0
                # Otherwise, reverse as many steps as possible: ty = ty % tx
                # But we need to ensure we don't go below sy
                ty %= tx
        
        # If we exit the loop, we've gone below the source point
        return False