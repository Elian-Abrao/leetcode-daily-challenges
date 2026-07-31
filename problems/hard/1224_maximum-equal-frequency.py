from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = {}
        freq = {}
        max_freq = 0
        result = 0
        
        for i, num in enumerate(nums):
            if num in count:
                old_freq = count[num]
                freq[old_freq] -= 1
                if freq[old_freq] == 0:
                    del freq[old_freq]
            
            count[num] = count.get(num, 0) + 1
            new_freq = count[num]
            freq[new_freq] = freq.get(new_freq, 0) + 1
            max_freq = max(max_freq, new_freq)
            
            length = i + 1
            distinct = len(count)
            
            # Check valid patterns
            # Case 1: All elements appear exactly once
            if max_freq == 1:
                result = length
            # Case 2: Only one distinct element
            elif distinct == 1:
                result = length
            # Case 3: All elements appear max_freq times, plus one extra element
            elif length == distinct * max_freq + 1:
                result = length
            # Case 4: All elements appear (max_freq - 1) times except one appears max_freq times
            elif length == (distinct - 1) * max_freq + 1:
                result = length
            # Case 5: Two different frequencies exist
            elif len(freq) == 2:
                freq_keys = list(freq.keys())
                f1, f2 = freq_keys[0], freq_keys[1]
                c1, c2 = freq[f1], freq[f2]
                
                # One element appears once, others appear same frequency
                if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                    result = length
                # One element appears one more time than others
                elif (f1 == f2 + 1 and c1 == 1) or (f2 == f1 + 1 and c2 == 1):
                    result = length
                # (distinct - 1) elements appear f times, 1 element appears f-1 times, and we can remove from any f
                elif (f1 == f2 + 1 and c2 == 1 and f1 * c1 == length - f2) or \
                     (f2 == f1 + 1 and c1 == 1 and f2 * c2 == length - f1):
                    result = length
        
        return result