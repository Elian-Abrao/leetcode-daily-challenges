class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        # A mountain must have at least 3 elements.
        if n < 3:
            return False

        # Climb from left until we stop increasing.
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be at the very start or end.
        if i == 0 or i == n - 1:
            return False

        # Descend from the peak until we stop decreasing.
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # If we reached the last element, it's a valid mountain.
        return i == n - 1