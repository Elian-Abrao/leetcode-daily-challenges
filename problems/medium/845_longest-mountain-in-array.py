class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        best = 0
        i = 1

        while i < n:
            # skip equal elements
            while i < n and arr[i] == arr[i-1]:
                i += 1

            if i < n and arr[i] > arr[i-1]:
                # decide if the mountain's base includes the previous element
                if i-1 == 0 or arr[i-1] < arr[i-2]:
                    # include the previous element as start
                    up = 1
                    i += 1
                else:
                    # start the mountain at the current element
                    up = 0
                    i += 1  # skip the first increase step

                # count increasing part
                while i < n and arr[i] > arr[i-1]:
                    up += 1
                    i += 1

                # count decreasing part
                down = 0
                while i < n and arr[i] < arr[i-1]:
                    down += 1
                    i += 1

                if up > 0 and down > 0:
                    best = max(best, up + down + 1)
            else:
                i += 1

        return best