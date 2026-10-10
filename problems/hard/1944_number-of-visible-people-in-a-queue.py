from __future__ import annotations


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)

        # Detect strictly decreasing array
        strictly_decreasing = True
        for i in range(1, n):
            if heights[i] >= heights[i - 1]:
                strictly_decreasing = False
                break
        if strictly_decreasing:
            return [n - 1 - i for i in range(n)]

        # Original monotonic stack algorithm
        answer = [0] * n
        stack: list[int] = []

        for i in range(n - 1, -1, -1):
            visible = 0
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                visible += 1
            if stack:
                visible += 1
            answer[i] = visible
            stack.append(i)

        return answer