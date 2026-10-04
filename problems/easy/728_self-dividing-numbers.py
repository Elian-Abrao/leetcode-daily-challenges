class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        """
        Returns all self-dividing numbers in the inclusive range [left, right].
        A self-dividing number is divisible by every one of its digits and
        does not contain the digit zero.
        """
        def is_self_dividing(num: int) -> bool:
            """Check if a number is self-dividing."""
            n = num
            # Extract each digit and test divisibility
            while n > 0:
                digit = n % 10
                # If digit is zero, number is invalid (cannot divide by 0)
                # If num is not divisible by this digit, it fails
                if digit == 0 or num % digit != 0:
                    return False
                n //= 10
            # A positive integer always has at least one digit,
            # so if we finish the loop, all digits passed.
            return True

        # Collect all qualifying numbers in the range
        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        return result