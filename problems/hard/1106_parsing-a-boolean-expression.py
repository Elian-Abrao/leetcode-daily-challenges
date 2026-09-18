class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        Evaluates a boolean expression with operators & (AND), | (OR), ! (NOT)
        using an iterative stack approach. 
        Time: O(n) where n = len(expression)
        Space: O(n) for the stack
        """
        # Stack holds intermediate results: boolean values as 't'/'f' strings,
        # and operators '&', '|', '!', '(' as markers.
        stack = []
        
        for ch in expression:
            if ch == ')':
                # Process one complete subexpression: collect all values
                # until the matching '(' and the operator before it.
                values = []
                # Pop until '(' is found
                while stack and stack[-1] != '(':
                    values.append(stack.pop())
                # Remove the '(' from the stack
                stack.pop()  # pops '('
                # Pop the operator that precedes '('
                operator = stack.pop()  # '&', '|', or '!'
                
                # Evaluate based on the operator.
                if operator == '&':
                    # AND: false if any 'f' exists
                    result = 't' if all(v == 't' for v in values) else 'f'
                elif operator == '|':
                    # OR: true if any 't' exists
                    result = 't' if any(v == 't' for v in values) else 'f'
                else:  # operator == '!'
                    # NOT: single operand (guaranteed by problem)
                    result = 't' if values[0] == 'f' else 'f'
                
                stack.append(result)
                
            elif ch == ',':
                # Commas are just separators; skip them.
                continue
            elif ch != '(':
                # Operators except '(' (which we push later on the stack separately)
                # Actually, we need to push '(' separately because it marks the beginning.
                # But the current character is either 't','f','&','|','!'.
                # We push them all; '(' will be handled later.
                stack.append(ch)
            else:  # ch == '('
                # '(' is pushed as a marker for the end of a subexpression.
                stack.append('(')
        
        # The final result is a single boolean value on top of the stack.
        # The problem guarantees valid input, so it's either 't' or 'f'.
        return stack[-1] == 't'