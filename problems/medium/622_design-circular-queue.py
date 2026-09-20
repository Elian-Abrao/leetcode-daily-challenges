class MyCircularQueue:
    """Circular queue (ring buffer) using a fixed-size array and modulo arithmetic."""

    def __init__(self, k: int):
        """
        Initialize the queue with capacity k.
        - head: index of the front element (next to dequeue)
        - tail: index of the next insertion position
        - size: number of elements currently stored
        """
        self.capacity = k
        self.queue = [0] * k          # preallocate storage
        self.head = 0
        self.tail = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """Insert an element at the rear. Returns True on success, False if full."""
        if self.isFull():
            return False
        self.queue[self.tail] = value
        # Advance tail circularly
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """Delete the front element. Returns True on success, False if empty."""
        if self.isEmpty():
            return False
        # Advance head circularly (value is overwritten later, no need to clear)
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """Return the front element, or -1 if empty."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Return the last element, or -1 if empty."""
        if self.isEmpty():
            return -1
        # tail points to next insertion spot, so the last element is one position behind
        last_index = (self.tail - 1 + self.capacity) % self.capacity
        return self.queue[last_index]

    def isEmpty(self) -> bool:
        """Check if the queue has no elements."""
        return self.size == 0

    def isFull(self) -> bool:
        """Check if the queue has reached its capacity."""
        return self.size == self.capacity