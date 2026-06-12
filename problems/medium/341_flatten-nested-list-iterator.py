from __future__ import annotations

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Use a stack to maintain the traversal state
        # Store elements in reverse order so we can pop from the end (LIFO)
        # This allows us to process left-to-right naturally
        self.stack = list(reversed(nestedList))
    
    def next(self) -> int:
        # hasNext() guarantees the top of stack is an integer
        # Simply pop and return it
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # Ensure the top of the stack is an integer (if stack is non-empty)
        # This may require unwrapping nested lists
        while self.stack:
            top = self.stack[-1]
            
            # If top is already an integer, we're ready
            if top.isInteger():
                return True
            
            # Top is a list, so we need to flatten it
            # Remove the list from stack
            self.stack.pop()
            
            # Push its contents onto the stack in reverse order
            # This maintains left-to-right order when popping
            nested_list = top.getList()
            for item in reversed(nested_list):
                self.stack.append(item)
        
        # Stack is empty, no more elements
        return False