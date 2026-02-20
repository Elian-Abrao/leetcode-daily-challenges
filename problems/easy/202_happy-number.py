class Solution:
    def isHappy(self, n: int) -> bool:
        # Use a set to detect cycles: if we revisit a number, we're in a loop
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            # compute sum of squares of digits of current n
            total = 0
            x = n
            while x:
                d = x % 10
                total += d * d
                x //= 10
            n = total
        # If we reached 1, it's happy; otherwise, we found a cycle
        return n == 1