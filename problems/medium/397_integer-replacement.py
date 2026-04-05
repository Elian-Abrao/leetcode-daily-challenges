class Solution:
    def integerReplacement(self, n: int) -> int:
        # Greedy bit-based strategy:
        # - Even numbers should always be halved immediately.
        # - For odd numbers, choose +/-1 to create more trailing zero bits,
        #   because that allows more future divisions by 2.
        steps = 0

        while n != 1:
            if n & 1 == 0:
                # Halving is always optimal for even values.
                n >>= 1
            else:
                # Special-case 3: going down is better than going up.
                # 3 -> 2 -> 1 takes 2 steps, while 3 -> 4 -> 2 -> 1 takes 3.
                if n == 3:
                    n -= 1
                # If the last two bits are 01, subtracting 1 creates more zeros.
                # Example: 5 (101) -> 4 (100).
                elif n & 3 == 1:
                    n -= 1
                else:
                    # If the last two bits are 11, adding 1 is usually better.
                    # Example: 7 (111) -> 8 (1000), enabling repeated halving.
                    n += 1
            steps += 1

        return steps