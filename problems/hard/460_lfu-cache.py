class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy head and tail for easier operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_first(self, node: Node) -> None:
        # Insert node right after head (most recently used position)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node: Node) -> None:
        # Remove node from the list
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_last(self) -> Node:
        # Remove and return the least recently used node (before tail)
        if self.size > 0:
            last_node = self.tail.prev
            self.remove(last_node)
            return last_node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # Track minimum frequency for O(1) eviction
        self.key_to_node = {}  # Map key -> Node
        self.freq_to_list = {}  # Map frequency -> DoublyLinkedList of nodes with that frequency
    
    def _update_freq(self, node: Node) -> None:
        # Remove node from current frequency list
        freq = node.freq
        self.freq_to_list[freq].remove(node)
        
        # If current frequency list becomes empty and it's the min frequency,
        # increment min_freq since this node is moving to freq+1
        if self.freq_to_list[freq].size == 0:
            del self.freq_to_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Increment node frequency and add to new frequency list
        node.freq += 1
        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = DoublyLinkedList()
        self.freq_to_list[node.freq].add_first(node)
    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            # Key exists: update value and frequency
            node = self.key_to_node[key]
            node.value = value
            self._update_freq(node)
        else:
            # Key doesn't exist: need to insert
            if len(self.key_to_node) >= self.capacity:
                # Evict least frequently used, least recently used key
                lfu_list = self.freq_to_list[self.min_freq]
                evicted_node = lfu_list.remove_last()
                del self.key_to_node[evicted_node.key]
            
            # Insert new node with frequency 1
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.min_freq = 1
            if 1 not in self.freq_to_list:
                self.freq_to_list[1] = DoublyLinkedList()
            self.freq_to_list[1].add_first(new_node)