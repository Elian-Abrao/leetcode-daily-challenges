from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge cases: if window size is 1, or nums is empty
        if not nums or k <= 0:
            return []
        
        dq = deque()  # stores indices of elements, values are in non-increasing order
        res = []
        
        for i, val in enumerate(nums):
            # Remove indices that are outside the current window [i-k+1, i]
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Maintain decreasing values in the deque
            # If current value is greater than values at back, pop smaller ones
            while dq and nums[dq[-1]] < val:
                dq.pop()
            
            dq.append(i)
            
            # Start recording results once the first window is fully formed
            if i >= k - 1:
                res.append(nums[dq[0]])  # The front of deque is the max for this window
        
        return res