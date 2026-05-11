class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes for each character
        self.children = {}
        # Flag to mark if this node represents the end of a valid word
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Initialize trie with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root and traverse/create nodes for each character
        node = self.root
        for char in word:
            # Create a new node if the character doesn't exist in current node's children
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the last node as end of word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Traverse the trie following the characters in word
        node = self.root
        for char in word:
            # If any character is not found, word doesn't exist
            if char not in node.children:
                return False
            node = node.children[char]
        # Word exists only if we reach a node marked as end of word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Traverse the trie following the characters in prefix
        node = self.root
        for char in prefix:
            # If any character is not found, no word with this prefix exists
            if char not in node.children:
                return False
            node = node.children[char]
        # If we successfully traversed all characters, prefix exists
        return True