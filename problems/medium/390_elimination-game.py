class Solution:
    def lastRemaining(self, n: int) -> int:
        # Track the first element in the current remaining sequence
        head = 1
        # Track the step size between consecutive elements
        step = 1
        # Track the remaining count of elements
        remaining = n
        # Track direction: True = left-to-right, False = right-to-left
        left_to_right = True
        
        # Continue elimination rounds until only one element remains
        while remaining > 1:
            # Update head if:
            # 1. Moving left-to-right (always removes first element)
            # 2. Moving right-to-left with odd count (head shifts)
            # When moving right-to-left with even count, head stays the same
            if left_to_right or remaining % 2 == 1:
                head += step
            
            # After each round, remaining elements are halved
            remaining //= 2
            # Step size doubles (distance between survivors increases)
            step *= 2
            # Alternate direction for next round
            left_to_right = not left_to_right
        
        return head