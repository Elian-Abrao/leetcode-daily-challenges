class Solution:
    def climbStairs(self, n: int) -> int:
        # Classic DP problem: to reach step n, we can arrive from step (n-1) or (n-2)
        # This gives us the recurrence: f(n) = f(n-1) + f(n-2)
        # This is essentially the Fibonacci sequence
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Use two variables to track the last two values instead of an array
        # This optimizes space complexity from O(n) to O(1)
        # prev2 represents f(i-2), prev1 represents f(i-1)
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2
        
        # Build up from step 3 to step n
        for i in range(3, n + 1):
            current = prev1 + prev2  # Ways to reach current step
            prev2 = prev1  # Shift window forward
            prev1 = current
        
        return prev1