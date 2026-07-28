class Solution:
    def deserialize(self, s: str):
        # Import NestedInteger from the module scope if available
        # On LeetCode, NestedInteger is predefined globally
        if 'NestedInteger' not in dir():
            # Try to get it from test environment
            import sys
            if hasattr(sys.modules.get('__main__'), 'NestedInteger'):
                global NestedInteger
                NestedInteger = sys.modules['__main__'].NestedInteger
        
        # Edge case: if s is just a number (no brackets), return a single integer
        if s[0] != '[':
            return NestedInteger(int(s))
        
        # Use a stack to handle nested structures
        stack = []
        i = 0
        
        while i < len(s):
            char = s[i]
            
            if char == '[':
                stack.append(NestedInteger())
                i += 1
                
            elif char == ']':
                if len(stack) > 1:
                    completed = stack.pop()
                    stack[-1].add(completed)
                i += 1
                
            elif char == ',':
                i += 1
                
            else:
                j = i
                if s[j] == '-':
                    j += 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                
                num = int(s[i:j])
                stack[-1].add(NestedInteger(num))
                i = j
        
        return stack[-1]