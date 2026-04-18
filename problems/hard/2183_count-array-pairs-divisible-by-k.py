from typing import List
from math import gcd


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Count frequency of gcd(nums[i], k) for all elements
        freq = {}
        for v in nums:
            g = gcd(v, k)
            freq[g] = freq.get(g, 0) + 1

        # Only divisors that actually appear matter for pairing
        divisors = sorted(freq.keys())

        ans = 0
        # Iterate over all pairs of gcd-values (including self-pairs)
        for i, d1 in enumerate(divisors):
            c1 = freq[d1]
            # Pairs (same gcd value)
            if (d1 * d1) % k == 0:
                ans += c1 * (c1 - 1) // 2

            # Pairs with a larger gcd value
            for d2 in divisors[i + 1:]:
                if (d1 * d2) % k == 0:
                    ans += c1 * freq[d2]

        return ans