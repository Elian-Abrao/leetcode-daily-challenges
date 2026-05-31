from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a hash map where the key is a canonical representation of the anagram group
        # and the value is the list of strings belonging to that group
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a canonical key for anagrams
            # All anagrams will have the same sorted representation
            # Example: "eat", "tea", "ate" all become "aet"
            key = tuple(sorted(s))
            
            # Append the original string to the group identified by this key
            anagram_groups[key].append(s)
        
        # Return all groups as a list of lists
        # The order of groups doesn't matter per problem statement
        return list(anagram_groups.values())