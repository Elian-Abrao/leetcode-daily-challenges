import heapq


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # Manacher for odd-length palindromes:
        # d1[i] = number of characters we can expand on each side of center i,
        # counting the center itself as radius 1.
        d1 = [0] * n
        left = 0
        right = -1
        for i in range(n):
            radius = 1 if i > right else min(d1[left + right - i], right - i + 1)
            while i - radius >= 0 and i + radius < n and s[i - radius] == s[i + radius]:
                radius += 1
            d1[i] = radius
            if i + radius - 1 > right:
                left = i - radius + 1
                right = i + radius - 1

        # max_end_exact[e] = longest odd palindrome ending exactly at index e.
        # For a center c with maximum right boundary R, every e in [c, R]
        # can use a palindrome of length 2 * (e - c) + 1.
        max_end_exact = [1] * n
        active = []
        for end in range(n):
            center = end
            radius = d1[center]
            max_right = center + radius - 1

            # Store the linear term so each active center contributes:
            # length = 2 * end + (1 - 2 * center)
            heapq.heappush(active, (-(1 - 2 * center), max_right))

            # Remove centers that cannot reach this end anymore.
            while active and active[0][1] < end:
                heapq.heappop(active)

            best_intercept = -active[0][0]
            max_end_exact[end] = 2 * end + best_intercept

        # max_start_exact[start] = longest odd palindrome starting exactly at index start.
        # Symmetrically, for center c with minimum left boundary L, every start in [L, c]
        # can use a palindrome of length 2 * (c - start) + 1.
        max_start_exact = [1] * n
        active = []
        for start in range(n - 1, -1, -1):
            center = start
            radius = d1[center]
            min_left = center - radius + 1

            # Each active center contributes:
            # length = -2 * start + (2 * center + 1)
            heapq.heappush(active, (-(2 * center + 1), min_left))

            # Remove centers whose palindrome starts strictly after this index.
            while active and active[0][1] > start:
                heapq.heappop(active)

            best_intercept = -active[0][0]
            max_start_exact[start] = best_intercept - 2 * start

        # best_left[i] = longest odd palindrome fully contained in s[0..i].
        best_left = [0] * n
        best_left[0] = max_end_exact[0]
        for i in range(1, n):
            best_left[i] = max(best_left[i - 1], max_end_exact[i])

        # best_right[i] = longest odd palindrome fully contained in s[i..n-1].
        best_right = [0] * n
        best_right[-1] = max_start_exact[-1]
        for i in range(n - 2, -1, -1):
            best_right[i] = max(best_right[i + 1], max_start_exact[i])

        # Split between i and i + 1, guaranteeing the two substrings do not intersect.
        answer = 0
        for i in range(n - 1):
            answer = max(answer, best_left[i] * best_right[i + 1])

        return answer