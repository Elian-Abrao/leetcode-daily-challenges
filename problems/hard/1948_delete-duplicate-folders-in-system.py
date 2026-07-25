from typing import List
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Build a trie structure to represent the folder hierarchy
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.to_delete = False
        
        root = TrieNode()
        
        # Step 1: Build the trie from all paths
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        
        # Step 2: Compute a hash for each subtree (bottom-up)
        # The hash represents the structure of subfolders beneath each node
        # Nodes with identical non-empty subtree structures will have the same hash
        def compute_hash(node):
            # If this is a leaf node (no children), return empty string
            if not node.children:
                return ""
            
            # Collect hashes of all children, sorted by folder name for consistency
            child_hashes = []
            for folder_name in sorted(node.children.keys()):
                child_node = node.children[folder_name]
                child_hash = compute_hash(child_node)
                # Include folder name and its subtree hash
                child_hashes.append((folder_name, child_hash))
            
            # Create a canonical representation of this subtree
            # Using tuple ensures deterministic hashing
            subtree_signature = str(child_hashes)
            return subtree_signature
        
        # Step 3: Group nodes by their subtree hash
        # Track which subtree structures appear more than once
        hash_to_nodes = defaultdict(list)
        
        def collect_hashes(node, hash_val):
            # Only consider non-empty subtrees (nodes with children)
            if hash_val and node.children:
                hash_to_nodes[hash_val].append(node)
            
            # Recursively process children
            for folder_name in node.children:
                child_node = node.children[folder_name]
                child_hash = compute_hash(child_node)
                collect_hashes(child_node, child_hash)
        
        # Compute hash for root's children
        for folder_name in root.children:
            child_node = root.children[folder_name]
            child_hash = compute_hash(child_node)
            collect_hashes(child_node, child_hash)
        
        # Step 4: Mark nodes for deletion if their subtree structure is duplicated
        for hash_val, nodes in hash_to_nodes.items():
            # If more than one node has the same non-empty subtree structure, mark all for deletion
            if len(nodes) > 1:
                for node in nodes:
                    node.to_delete = True
        
        # Step 5: Collect all remaining paths (not marked for deletion)
        # If a node is marked, all its descendants are implicitly deleted too
        result = []
        
        def collect_paths(node, current_path):
            # If current node is marked for deletion, skip it and all descendants
            if node.to_delete:
                return
            
            # Add current path if it's not empty (not at root)
            if current_path:
                result.append(current_path[:])
            
            # Recursively collect paths from children
            for folder_name in sorted(node.children.keys()):
                child_node = node.children[folder_name]
                current_path.append(folder_name)
                collect_paths(child_node, current_path)
                current_path.pop()
        
        # Start collection from root
        collect_paths(root, [])
        
        return result