class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        Compute probability that total points are <= n when game stops.
        Game stops when points >= k. Each draw adds [1, maxPts] uniformly.
        
        Use dynamic programming with sliding window sum for O(n) time.
        dp[i] = probability of reaching exactly i points during the game.
        We only care about probabilities before stopping (i < k).
        """
        # If k == 0, Alice already has 0 points which is >= k, so she stops immediately.
        # Probability that 0 <= n is always 1.0.
        if k == 0:
            return 1.0
        
        # If n >= k + maxPts - 1, it's guaranteed that final score <= n
        # because max possible final score is k + maxPts - 1 (if just below k then draw max)
        if n >= k + maxPts - 1:
            return 1.0
        
        # dp[i] = probability of having exactly i points at some point
        # We only need up to n (since we stop at k and n >= k per constraints,
        # but n can be less than k? Actually constraints say k <= n, but we handle generally).
        # We'll allocate up to n since final scores can't exceed n in the probability we need.
        max_score = n  # we only need probabilities up to n to compute answer
        
        dp = [0.0] * (max_score + 1)
        dp[0] = 1.0  # start with 0 points with probability 1
        
        # Sliding window sum of dp values for the last maxPts positions
        # This avoids O(k * maxPts) inner loop
        window_sum = 0.0
        # We'll iterate i from 0 to min(k-1, max_score) building probabilities
        # For each state i < k, we transition to i+1 ... i+maxPts
        # Instead of iterating transitions forward, we push contributions forward
        # using a sliding window when processing each i.
        
        # We'll process states in increasing order of i.
        # When we are at state i (i < k), we know dp[i] is final (no more transitions from lower states)
        # We add dp[i] / maxPts to states i+1...i+maxPts.
        # To do this efficiently, we maintain a running sum of "contributions" to the current cell.
        
        # Approach: iterate i from 0 to min(k-1, max_score).
        # At each i, we add dp[i] to window_sum (it will be distributed to future states).
        # Then dp[i] = current contribution from window (since we are processing i, 
        # contributions to i have been accumulated).
        # Actually, the standard solution: 
        # Let dp[i] be prob of reaching i (including before stopping).
        # For i < k, we distribute dp[i]/maxPts to next maxPts states.
        # We use a sliding window sum 'running_sum' = sum_{j=1}^{maxPts} dp[i-j] / maxPts
        # when computing dp[i] for i > 0.
        
        # Reset for clearer sliding window:
        dp = [0.0] * (max_score + 1)
        dp[0] = 1.0
        
        # 'window' holds the sum of (dp[i-1] + ... + dp[i-maxPts]) / maxPts
        # This is the probability mass flowing into state i from previous states.
        window = 0.0
        
        for i in range(1, max_score + 1):
            # Add contribution from state i-1 to window (if i-1 < k, it distributes)
            if i - 1 < k:
                window += dp[i - 1] / maxPts
            
            # Remove contribution that falls out of the window (beyond maxPts steps back)
            if i - 1 - maxPts >= 0:
                if i - 1 - maxPts < k:
                    window -= dp[i - 1 - maxPts] / maxPts
            
            # Current probability of reaching i is the window sum
            dp[i] = window
        
        # Answer: sum of probabilities of final scores (k to n inclusive)
        # Final scores are states >= k that are reachable.
        # Also includes states < k if k > n? But constraints say k <= n typically.
        # Sum probabilities for all scores from k to n.
        # However, dp[i] for i >= k represents probability of *stopping* at i?
        # No, dp[i] above is probability of ever reaching i (including intermediate).
        # We need probability that final score <= n.
        # The process stops at the first time score >= k.
        # So for i >= k, dp[i] as computed above (with transitions only from i < k)
        # is exactly the probability of stopping at i, because once >= k we stop.
        # Since we only add dp[i-1]/maxPts for i-1 < k, dp[i] correctly captures
        # probability of first reaching i when i >= k.
        
        result = 0.0
        for i in range(k, min(n, max_score) + 1):
            result += dp[i]
        
        # Also, if k == 0 case handled above; but also if n < k (shouldn't happen per constraints)
        # we would need sum of dp[0..n] but dp[0]=1.0 if k=0, but k>0 here.
        
        return result