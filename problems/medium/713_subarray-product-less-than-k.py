class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays whose product is strictly less than k.

        Approach: sliding window (two pointers). For each right index, maintain a window
        [left, right] such that the product of all elements in the window is < k.
        The number of valid subarrays ending at right is (right - left + 1).
        Sum these counts over all right positions.

        Why it works:
        - All elements are positive (>=1), so the product increases monotonically as we
          expand the window to the right. Therefore, for a fixed left, the product with
          more elements never decreases.
        - When the product becomes >= k, we move left forward (shrinking from the left)
          to reduce the product. This ensures the window always satisfies product < k.
        - All subarrays ending at right that are completely inside [left, right] are valid
          because any subarray that starts between left and right and ends at right will have
          product <= window product (since it's a subarray of the current valid window and
          all numbers are positive, its product is <= product of entire window, which is < k).
          So the count of new valid subarrays ending at right is exactly right - left + 1.

        Edge cases:
        - k <= 1: no subarray can have product < k (minimum product is 1). The algorithm
          will immediately move left to right+1 and right-left+1 becomes 0, so total = 0.
        - Single element: handled normally.
        - Large input: O(n) time, O(1) space.
        - Product may become large, but we stop expanding when product >= k, and k <= 1e6,
          so the product never exceeds ~1e9. Python handles big integers natively; no overflow.

        :param nums: List of positive integers (1 <= nums[i] <= 1000)
        :param k: Threshold (0 <= k <= 10^6)
        :return: Number of contiguous subarrays with product < k
        """
        # If k is 0 or 1, no product can be < k because minimum product is 1.
        if k <= 1:
            return 0

        ans = 0          # total count of valid subarrays
        product = 1      # product of elements in the current window
        left = 0         # left boundary of the window (inclusive)

        # Expand the window by moving the right boundary.
        for right, val in enumerate(nums):
            product *= val

            # While product is too large, shrink the window from the left.
            # Since all elements are >=1, this will eventually make product < k.
            while product >= k and left <= right:
                # Divide by the element leaving the window.
                product //= nums[left]
                left += 1

            # After the while loop, product < k holds for the window [left, right].
            # All subarrays that start at any index between left and right (inclusive)
            # and end at 'right' have product < k.
            # The number of such starting positions is: right - left + 1.
            ans += right - left + 1

        return ans