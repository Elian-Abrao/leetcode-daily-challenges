class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Greedy: plant a flower whenever the current plot and both neighbors are empty.
        # This yields the maximum possible number of new plants, so checking against n is sufficient.
        planted = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 1:
                continue

            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                planted += 1
                if planted >= n:
                    return True

        return planted >= n