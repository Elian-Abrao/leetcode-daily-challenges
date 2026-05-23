from typing import List
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # This is a geometric median problem (Fermat-Weber problem)
        # We use gradient descent to find the optimal center location
        # that minimizes the sum of Euclidean distances to all points
        
        # Helper function to compute total distance from point (x, y) to all positions
        def total_distance(x: float, y: float) -> float:
            dist_sum = 0.0
            for px, py in positions:
                dist_sum += math.sqrt((x - px) ** 2 + (y - py) ** 2)
            return dist_sum
        
        # Helper function to compute gradient at point (x, y)
        # Gradient of sum of distances: ∂f/∂x = Σ (x - x_i) / dist_i
        def compute_gradient(x: float, y: float) -> tuple:
            grad_x = 0.0
            grad_y = 0.0
            for px, py in positions:
                dist = math.sqrt((x - px) ** 2 + (y - py) ** 2)
                # Avoid division by zero when point coincides with a customer
                if dist > 1e-9:
                    grad_x += (x - px) / dist
                    grad_y += (y - py) / dist
            return grad_x, grad_y
        
        # Initialize center at the centroid (mean position)
        # This is a good starting point for gradient descent
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        
        # Gradient descent parameters
        learning_rate = 1.0  # Initial step size
        epsilon = 1e-7  # Convergence threshold
        
        # Perform gradient descent until convergence
        while True:
            grad_x, grad_y = compute_gradient(x, y)
            
            # Calculate gradient magnitude
            grad_magnitude = math.sqrt(grad_x ** 2 + grad_y ** 2)
            
            # Stop if gradient is very small (we're at a minimum)
            if grad_magnitude < epsilon:
                break
            
            # Move in the opposite direction of gradient
            new_x = x - learning_rate * grad_x
            new_y = y - learning_rate * grad_y
            
            # Check if we're making progress
            current_dist = total_distance(x, y)
            new_dist = total_distance(new_x, new_y)
            
            # If the new position is better, accept it
            if new_dist < current_dist:
                x, y = new_x, new_y
                # Optionally increase learning rate for faster convergence
                learning_rate *= 1.01
            else:
                # If we overshot, reduce learning rate and try again
                learning_rate *= 0.5
                # Stop if learning rate becomes too small
                if learning_rate < epsilon:
                    break
        
        # Return the minimum sum of distances
        return total_distance(x, y)