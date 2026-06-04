class MyQueue:

    def __init__(self):
        # Stack for incoming elements (push operations)
        self.stack_in = []
        # Stack for outgoing elements (pop/peek operations)
        self.stack_out = []

    def push(self, x: int) -> None:
        # Always push new elements to stack_in
        # Time: O(1)
        self.stack_in.append(x)

    def pop(self) -> int:
        # Move elements from stack_in to stack_out if stack_out is empty
        # This reverses the order, making LIFO -> FIFO
        self._transfer_if_needed()
        # Pop from stack_out gives us the front of the queue
        # Amortized O(1): each element is moved at most once
        return self.stack_out.pop()

    def peek(self) -> int:
        # Similar to pop but without removing the element
        self._transfer_if_needed()
        # Peek at the top of stack_out (front of queue)
        # Amortized O(1)
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        # Time: O(1)
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    
    def _transfer_if_needed(self) -> None:
        # Only transfer elements when stack_out is empty
        # This ensures we maintain the correct FIFO order
        if not self.stack_out:
            # Move all elements from stack_in to stack_out
            # Reverses order: oldest element ends up on top of stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())