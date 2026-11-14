from __future__ import annotations
from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        # result[i] = time when car i collides with the next car, or -1.0 if never
        result = [-1.0] * n
        # stack indices of cars that have not yet been absorbed from the right
        stack = []  # will hold indices of cars (or fleets) still "alive"

        for i in range(n - 1, -1, -1):
            pos_i, speed_i = cars[i]

            # try to find which car ahead will be the first to collid with i
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]

                if speed_i <= speed_j:
                    # car i is not faster than the car directly ahead
                    # if that car never collides, i will never catch it
                    if result[j] == -1.0:
                        # no collision possible
                        break
                    else:
                        # the car ahead will merge with its own target before i could reach it
                        # so that car is no longer a valid obstacle, discard it
                        stack.pop()
                        continue
                else:
                    # car i is faster -> compute catch-up time
                    t = (pos_j - pos_i) / (speed_i - speed_j)
                    # if the car ahead never collides or collides after t, then i catches it now
                    if result[j] == -1.0 or t <= result[j]:
                        result[i] = t
                        break
                    else:
                        # the ahead car will merge first, so it disappears from consideration
                        stack.pop()
                        continue

            # after the while loop, if result[i] was not set, it remains -1.0 (never collides)
            # push the current car onto the stack (it will be considered by future left cars)
            stack.append(i)

        return result