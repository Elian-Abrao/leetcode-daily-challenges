class Solution:
    def numSquares(self, n: int) -> int:
        # A perfect square itself needs exactly one number.
        root = int(n ** 0.5)
        if root * root == n:
            return 1

        # Remove factors of 4 first.
        # By Lagrange/Legendre theory, this normalization preserves the answer
        # with respect to the special "needs 4 squares" form.
        reduced = n
        while reduced % 4 == 0:
            reduced //= 4

        # Legendre's three-square theorem:
        # numbers of the form 4^a * (8b + 7) need exactly 4 squares.
        if reduced % 8 == 7:
            return 4

        # Check whether the answer is 2:
        # n = a^2 + b^2 for some integers a, b.
        # This is enough because after excluding 1 and 4,
        # the answer must be 2 or 3.
        limit = int(n ** 0.5)
        for a in range(1, limit + 1):
            remainder = n - a * a
            b = int(remainder ** 0.5)
            if b * b == remainder:
                return 2

        # If not 1, not 2, and not forced to 4, then it must be 3.
        return 3