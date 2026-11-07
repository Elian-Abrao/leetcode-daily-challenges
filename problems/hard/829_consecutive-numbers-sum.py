class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # A block of k positive integers starting at a has sum:
        #   n = k*a + k*(k-1)//2
        # => 2n = k * (2a + k - 1)
        # Let m = 2a + k - 1. For a valid block, m > k and m - k is odd.
        # So count opposite-parity factor pairs (k, m) of 2n.

        twice_n = 2 * n
        ways = 0

        # The length k is always the smaller factor, so k < sqrt(2n).
        k = 1
        while k * k < twice_n:
            if twice_n % k == 0:
                m = twice_n // k
                # Opposite parity means m-k is odd, so a = (m-k+1)/2 is a positive integer.
                if (m - k) % 2 == 1:
                    ways += 1
            k += 1

        # Time: O(sqrt(n)), extra space: O(1)
        return ways