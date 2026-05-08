from typing import List
from collections import defaultdict
import re

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # Build evaluation map for immediate substitution
        eval_map = dict(zip(evalvars, evalints))
        
        # Polynomial representation: dict mapping tuple of variables (sorted) to coefficient
        class Poly:
            def __init__(self, terms=None):
                self.terms = defaultdict(int)
                if terms:
                    for key, val in terms.items():
                        if val != 0:
                            self.terms[key] = val
            
            def __add__(self, other):
                result = Poly()
                for key, val in self.terms.items():
                    result.terms[key] += val
                for key, val in other.terms.items():
                    result.terms[key] += val
                result.terms = defaultdict(int, {k: v for k, v in result.terms.items() if v != 0})
                return result
            
            def __sub__(self, other):
                result = Poly()
                for key, val in self.terms.items():
                    result.terms[key] += val
                for key, val in other.terms.items():
                    result.terms[key] -= val
                result.terms = defaultdict(int, {k: v for k, v in result.terms.items() if v != 0})
                return result
            
            def __mul__(self, other):
                result = Poly()
                for key1, val1 in self.terms.items():
                    for key2, val2 in other.terms.items():
                        new_key = tuple(sorted(key1 + key2))
                        result.terms[new_key] += val1 * val2
                result.terms = defaultdict(int, {k: v for k, v in result.terms.items() if v != 0})
                return result
            
            def to_list(self):
                if not self.terms:
                    return []
                
                items = []
                for vars_tuple, coef in self.terms.items():
                    degree = len(vars_tuple)
                    items.append((degree, vars_tuple, coef))
                
                items.sort(key=lambda x: (-x[0], x[1]))
                
                result = []
                for degree, vars_tuple, coef in items:
                    if vars_tuple:
                        var_str = '*'.join(vars_tuple)
                        result.append(f"{coef}*{var_str}")
                    else:
                        result.append(str(coef))
                
                return result
        
        def parse_atom(token):
            if token.lstrip('-').isdigit():
                return Poly({(): int(token)})
            else:
                if token in eval_map:
                    return Poly({(): eval_map[token]})
                else:
                    return Poly({(token,): 1})
        
        # Tokenize expression - handle parentheses and operators
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
            elif expression[i] in '()+-*':
                tokens.append(expression[i])
                i += 1
            else:
                # Read a number or variable
                j = i
                while j < len(expression) and not expression[j].isspace() and expression[j] not in '()+-*':
                    j += 1
                tokens.append(expression[i:j])
                i = j
        
        self.index = 0
        
        def parse_expression():
            left = parse_term()
            while self.index < len(tokens) and tokens[self.index] in ['+', '-']:
                op = tokens[self.index]
                self.index += 1
                right = parse_term()
                if op == '+':
                    left = left + right
                else:
                    left = left - right
            return left
        
        def parse_term():
            left = parse_factor()
            while self.index < len(tokens) and tokens[self.index] == '*':
                self.index += 1
                right = parse_factor()
                left = left * right
            return left
        
        def parse_factor():
            token = tokens[self.index]
            if token == '(':
                self.index += 1
                result = parse_expression()
                self.index += 1  # skip ')'
                return result
            else:
                self.index += 1
                return parse_atom(token)
        
        poly = parse_expression()
        return poly.to_list()