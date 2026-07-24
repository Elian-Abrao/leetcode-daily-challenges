from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list (though constraints guarantee at least 1 element)
        if not strs:
            return ""
        
        # Edge case: if any string is empty, no common prefix exists
        if any(s == "" for s in strs):
            return ""
        
        # Start with the first string as the initial candidate prefix
        # We'll progressively reduce it as we compare with other strings
        prefix = strs[0]
        
        # Compare the current prefix with each subsequent string
        for i in range(1, len(strs)):
            # While the current string doesn't start with our prefix candidate,
            # shorten the prefix by removing the last character
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
        
        return prefix