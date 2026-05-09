class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = []
        # Auxiliary stack to track minimum at each level
        # min_stack[i] holds the minimum value in stack[0:i+1]
        self.min_stack = []

    def push(self, val: int) -> None:
        # Always push to main stack
        self.stack.append(val)
        
        # For min_stack, push the new minimum
        # If min_stack is empty, val is the minimum
        # Otherwise, compare val with current minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Remove from both stacks to maintain synchronization
        # The problem guarantees pop is only called on non-empty stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return top element without removing it
        # The problem guarantees top is only called on non-empty stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The top of min_stack always holds the current minimum
        # O(1) access since we maintain it during push/pop
        return self.min_stack[-1]