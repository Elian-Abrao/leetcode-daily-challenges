from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Trie node structure for binary representation of numbers
        class TrieNode:
            def __init__(self):
                self.children = {}  # 0 or 1 as keys
                
        class Trie:
            def __init__(self):
                self.root = TrieNode()
                
            def insert(self, num):
                # Insert number into trie (binary representation, 31 bits for max 10^9)
                node = self.root
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node.children:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                    
            def find_max_xor(self, num):
                # Find maximum XOR of num with any number in the trie
                if not self.root.children:
                    return -1
                    
                node = self.root
                result = 0
                
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    # To maximize XOR, we want the opposite bit
                    target_bit = 1 - bit
                    
                    if target_bit in node.children:
                        result |= (1 << i)
                        node = node.children[target_bit]
                    else:
                        # Take the only available path
                        node = node.children[bit]
                        
                return result
        
        # Sort nums to process them in increasing order
        sorted_nums = sorted(nums)
        
        # Augment queries with their original indices to maintain order in result
        # Format: (xi, mi, original_index)
        indexed_queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        
        # Sort queries by mi (constraint) to process in increasing order
        indexed_queries.sort(key=lambda q: q[1])
        
        # Initialize result array with -1 (default for impossible queries)
        result = [-1] * len(queries)
        
        trie = Trie()
        nums_idx = 0
        
        # Process each query in sorted order by constraint mi
        for x, m, original_idx in indexed_queries:
            # Insert all numbers <= m into the trie
            while nums_idx < len(sorted_nums) and sorted_nums[nums_idx] <= m:
                trie.insert(sorted_nums[nums_idx])
                nums_idx += 1
            
            # Find maximum XOR with x using all numbers currently in trie
            max_xor = trie.find_max_xor(x)
            result[original_idx] = max_xor
            
        return result