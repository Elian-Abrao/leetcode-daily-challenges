from collections import deque

class MyStack:

    def __init__(self):
        # Use a single queue to simulate stack behavior
        # We'll rotate elements during push to maintain LIFO order
        self.queue = deque()

    def push(self, x: int) -> None:
        # Add the new element to the back of the queue
        self.queue.append(x)
        
        # Rotate all elements that were added before this one
        # This ensures the newest element ends up at the front
        # After rotation, the queue front acts as the stack top
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Since push maintains LIFO order with newest at front,
        # we can simply pop from the front (standard queue operation)
        return self.queue.popleft()

    def top(self) -> int:
        # Peek at the front element without removing it
        # This is the most recently pushed element due to our push strategy
        return self.queue[0]

    def empty(self) -> bool:
        # Check if queue has no elements
        return len(self.queue) == 0