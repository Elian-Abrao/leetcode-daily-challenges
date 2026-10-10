class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        """
        Returns the minimal length of a contiguous subarray that has the same
        degree (maximum frequency) as the whole array.
        """
        # Track for each value: [first_index, last_index, frequency]
        info = {}

        # Single pass: record first/last occurrence and count
        for i, val in enumerate(nums):
            if val not in info:
                # First time seen: first = last = i, count = 1
                info[val] = [i, i, 1]
            else:
                entry = info[val]
                entry[1] = i          # update last occurrence
                entry[2] += 1         # increment frequency

        # Determine the maximum frequency (degree)
        degree = 0
        for entry in info.values():
            if entry[2] > degree:
                degree = entry[2]

        # Among values achieving the degree, find minimal subarray length
        min_len = len(nums)  # upper bound
        for entry in info.values():
            if entry[2] == degree:
                # length = last - first + 1
                length = entry[1] - entry[0] + 1
                if length < min_len:
                    min_len = length

        return min_len