class Solution:
    def evaluate(self, expression: str) -> int:
        def parse_tokens(expr):
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i] == '(':
                    tokens.append('(')
                    i += 1
                elif expr[i] == ')':
                    tokens.append(')')
                    i += 1
                elif expr[i] == ' ':
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j] not in '() ':
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
            return tokens
        
        def is_number(token):
            if not token or token in ('(', ')'):
                return False
            if token[0] == '-':
                return len(token) > 1 and token[1:].isdigit()
            return token.isdigit()
        
        def evaluate_expr(tokens, index, scope):
            token = tokens[index]
            
            # Case 1: Integer literal
            if is_number(token):
                return int(token), index + 1
            
            # Case 2: Variable reference
            if token not in ('(', ')'):
                return scope[token], index + 1
            
            # Case 3: Parenthesized expression
            if token == '(':
                index += 1  # skip '('
                op = tokens[index]
                index += 1  # skip operation keyword
                
                if op == 'let':
                    new_scope = scope.copy()
                    
                    while True:
                        # Check if we've reached the final expression
                        # Look ahead to see if this could be a variable assignment
                        if tokens[index] == ')':
                            index += 1
                            return 0, index
                        
                        # Save current position
                        save_index = index
                        
                        # Check if this is a variable name (not a number or subexpression)
                        if tokens[index] != '(' and not is_number(tokens[index]):
                            var_name = tokens[index]
                            index += 1
                            
                            # Check if next token is ')' - if so, var_name is the final expression
                            if tokens[index] == ')':
                                result = new_scope.get(var_name, 0) if var_name in new_scope else int(var_name) if is_number(var_name) else new_scope[var_name]
                                index += 1
                                return result, index
                            
                            # Otherwise, evaluate the value for this variable
                            value, index = evaluate_expr(tokens, index, new_scope)
                            new_scope[var_name] = value
                        else:
                            # This is the final expression (number or subexpression)
                            result, index = evaluate_expr(tokens, save_index, new_scope)
                            if tokens[index] == ')':
                                index += 1
                            return result, index
                
                elif op == 'add':
                    val1, index = evaluate_expr(tokens, index, scope)
                    val2, index = evaluate_expr(tokens, index, scope)
                    index += 1  # skip ')'
                    return val1 + val2, index
                
                elif op == 'mult':
                    val1, index = evaluate_expr(tokens, index, scope)
                    val2, index = evaluate_expr(tokens, index, scope)
                    index += 1  # skip ')'
                    return val1 * val2, index
            
            return 0, index
        
        tokens = parse_tokens(expression)
        result, _ = evaluate_expr(tokens, 0, {})
        return result