class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Compute the sum of the first valid window.
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window one element at a time.
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        # All windows have length exactly k, so the maximum average
        # is simply the maximum window sum divided by k.
        return max_sum / k