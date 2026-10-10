class MyCircularDeque:
    """Circular double-ended queue with fixed capacity."""

    def __init__(self, k: int):
        # Use a fixed-size list to store elements.
        self.capacity = k
        self.arr = [0] * k
        # `front` and `rear` always point to the first and last element when non-empty.
        # When empty, their values are undefined (we check `size` before accessing them).
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        # Insert at the front if space is available.
        if self.isFull():
            return False
        if self.isEmpty():
            # First element: front and rear both point to index 0.
            self.front = self.rear = 0
        else:
            # Move front backward (circularly) and place the value.
            self.front = (self.front - 1) % self.capacity
        self.arr[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        # Insert at the rear if space is available.
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        # Remove the front element if the deque is not empty.
        if self.isEmpty():
            return False
        # After removal, if the deque becomes empty, no need to change pointers;
        # they will be reset on next insertion.
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        # Remove the rear element if the deque is not empty.
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        # Return the front element, or -1 if empty.
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        # Return the rear element, or -1 if empty.
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity