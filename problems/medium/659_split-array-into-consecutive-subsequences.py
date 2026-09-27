from collections import defaultdict

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        # freq[x] = how many copies of x are still available
        freq = defaultdict(int)
        for val in nums:
            freq[val] += 1

        # need[x] = how many open subsequences are waiting for x as the next element
        need = defaultdict(int)

        for val in nums:
            # If no copies of val are left, skip (it was already consumed earlier)
            if freq[val] == 0:
                continue

            # Prefer to extend an existing subsequence if possible
            if need[val] > 0:
                # Use this copy of val to satisfy a subsequence waiting for val
                need[val] -= 1
                freq[val] -= 1
                # Now this subsequence will need val+1 next
                need[val + 1] += 1

            # Cannot extend – try to start a new subsequence of length >=3
            elif freq[val + 1] > 0 and freq[val + 2] > 0:
                # Consume val, val+1, val+2 to form a new subsequence
                freq[val] -= 1
                freq[val + 1] -= 1
                freq[val + 2] -= 1
                # This subsequence now waits for val+3 as the next element
                need[val + 3] += 1

            else:
                # Neither extension nor new subsequence possible
                return False

        return True