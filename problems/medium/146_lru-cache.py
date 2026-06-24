class LRUCache:
    
    def __init__(self, capacity: int):
        # Core data structures for O(1) get and put operations
        self.capacity = capacity
        self.cache = {}  # Maps key -> DLL node
        
        # Doubly linked list to maintain access order
        # Most recent at tail, least recent at head
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        # If key exists, move to most recent position and return value
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        # If key exists, update value and move to most recent position
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add_to_tail(node)
        else:
            # Create new node and add to most recent position
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_tail(node)
            
            # If capacity exceeded, evict least recently used (at head)
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
    
    def _remove(self, node):
        # Remove node from its current position in DLL
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_tail(self, node):
        # Add node right before tail (most recent position)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


class Node:
    # Doubly linked list node to store key-value pairs
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None