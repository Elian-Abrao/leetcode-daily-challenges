from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Early exit: if endWord not in wordList, no valid transformation exists
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        # Build a generic pattern mapping for efficient neighbor lookup
        # E.g., "hot" -> ["*ot", "h*t", "ho*"]
        # This avoids O(N) scan for each word to find neighbors
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        # BFS from beginWord to find shortest path
        queue = deque([(beginWord, 1)])  # (current_word, path_length)
        visited = {beginWord}
        
        while queue:
            current_word, length = queue.popleft()
            
            # Try all possible one-letter transformations
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Get all words matching this pattern
                for neighbor in pattern_map[pattern]:
                    # Check if we reached the target
                    if neighbor == endWord:
                        return length + 1
                    
                    # Add unvisited neighbors to queue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                
                # Clear pattern to avoid revisiting in future iterations
                # This optimization prevents redundant checks
                pattern_map[pattern] = []
        
        # No path found from beginWord to endWord
        return 0