class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        # Simulate a stack and attempt to match the pop sequence.
        # We push elements from 'pushed' one by one. After each push,
        # while the stack top matches the next element to pop, we pop it.
        # If at the end the stack is empty, the sequence is valid.
        
        stack = []               # Simulated stack (list as stack, top is end)
        pop_index = 0            # Current position in popped array
        
        for num in pushed:
            # Push current element onto stack
            stack.append(num)
            
            # Greedily pop while top matches the next needed pop value
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        # If all pushes and pops matched perfectly, stack will be empty
        return not stack