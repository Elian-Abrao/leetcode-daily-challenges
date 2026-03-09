class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_under_prefix(prefix: int) -> int:
            # Count how many numbers in [1, n] start with this prefix.
            # We expand interval [prefix, prefix + 1) level by level in the
            # implicit lexicographical trie.
            count = 0
            current = prefix
            next_prefix = prefix + 1

            while current <= n:
                # At each depth, valid numbers lie in [current, next_prefix).
                # Clamp the right boundary by n + 1 because n is inclusive.
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10

            return count

        # Lexicographical traversal starts at 1.
        current = 1
        k -= 1  # We already stand on the 1st lexicographical number.

        while k > 0:
            steps = count_under_prefix(current)

            if steps <= k:
                # Skip the whole subtree rooted at current and move to next sibling.
                current += 1
                k -= steps
            else:
                # The answer is inside this subtree; go to its first child.
                current *= 10
                k -= 1  # Consuming the child node itself in lexicographical order.

        return current