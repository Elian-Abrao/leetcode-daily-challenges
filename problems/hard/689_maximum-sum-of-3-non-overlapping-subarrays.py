from __future__ import annotations

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # Precompute sums of all windows of length k
        window_sums = [0] * (n - k + 1)
        cur = sum(nums[:k])
        window_sums[0] = cur
        for i in range(1, n - k + 1):
            # slide window: remove left, add right
            cur += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = cur

        m = len(window_sums)  # number of possible start positions

        # left[i] = best start index (smallest if tie) among windows 0..i
        left = [0] * m
        best_idx = 0
        best_sum = window_sums[0]
        for i in range(m):
            # if equal sum, keep the smaller index (lexicographically smaller)
            if window_sums[i] > best_sum:
                best_sum = window_sums[i]
                best_idx = i
            elif window_sums[i] == best_sum and i < best_idx:
                best_idx = i
            left[i] = best_idx

        # right[i] = best start index (smallest if tie) among windows i..m-1
        right = [0] * m
        best_idx = m - 1
        best_sum = window_sums[m - 1]
        for i in range(m - 1, -1, -1):
            if window_sums[i] > best_sum:
                best_sum = window_sums[i]
                best_idx = i
            elif window_sums[i] == best_sum and i < best_idx:
                best_idx = i
            right[i] = best_idx

        # Try every possible middle window
        max_total = -1
        answer = [0, 0, 0]  # placeholder
        # middle window can start from k to n-2k (so indices k .. m-k-1)
        for mid in range(k, m - k):   # ensures left and right have room
            l = left[mid - k]
            r = right[mid + k]
            total = window_sums[l] + window_sums[mid] + window_sums[r]
            if total > max_total:
                max_total = total
                answer = [l, mid, r]
            elif total == max_total:
                # Lexicographically smallest triple
                candidate = [l, mid, r]
                if candidate < answer:  # Python list comparison works lexicographically
                    answer = candidate

        return answer