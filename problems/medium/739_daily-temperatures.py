from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        
        # Monotonic decreasing stack storing indices
        # Stack holds indices where we haven't found a warmer day yet
        stack = []
        
        for i in range(n):
            # While current temperature is warmer than temperature at stack top
            # we've found the answer for those previous days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            
            # Push current index to stack, waiting for its warmer day
            stack.append(i)
        
        # Remaining indices in stack have no warmer future day (answer stays 0)
        return answer