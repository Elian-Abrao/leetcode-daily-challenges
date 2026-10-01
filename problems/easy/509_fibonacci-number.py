class Solution:
    def fib(self, n: int) -> int:
        # Base cases: F(0) = 0, F(1) = 1
        if n < 2:
            return n
        
        # Iterative bottom-up DP using constant space
        # Keep only the two most recent Fibonacci numbers
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            # Compute next Fibonacci number as sum of previous two
            prev, curr = curr, prev + curr
        
        return curr