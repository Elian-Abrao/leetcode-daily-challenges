from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        """
        Parse and evaluate a brace-expansion grammar using a recursive descent
        parser. The grammar:
        
        expr    -> term (',' term)*      # union
        term    -> factor factor*        # concatenation (cartesian product)
        factor  -> letter | '{' expr '}' 
        
        Returns a sorted list of unique expanded strings.
        """
        
        # Use an index pointer for efficient parsing without substring copies.
        self.idx = 0
        self.expr = expression
        self.n = len(expression)
        
        parsed_set = self._parse_expr()
        # Return sorted list as required.
        return sorted(parsed_set)
    
    def _parse_expr(self) -> set:
        """
        expr -> term (',' term)*
        Returns the union of all comma-separated terms.
        """
        # Start with the first term.
        result = self._parse_term()
        
        # While there is a comma, union with the next term.
        while self.idx < self.n and self.expr[self.idx] == ',':
            self.idx += 1  # consume ','
            result |= self._parse_term()
        
        return result
    
    def _parse_term(self) -> set:
        """
        term -> factor factor*
        Returns the Cartesian product (concatenation) of consecutive factors.
        The identity for concatenation is a set containing the empty string,
        but since we always have at least one factor, we start with that.
        """
        # Parse the first factor.
        factors = [self._parse_factor()]
        
        # Continue while the next character could start another factor.
        # A factor can start with a letter or an opening brace.
        while self.idx < self.n and self.expr[self.idx] not in (',', '}'):
            factor = self._parse_factor()
            factors.append(factor)
        
        # Compute Cartesian product of all factors.
        result = {''}
        for factor_set in factors:
            # Concatenate every word from result with every word from factor_set.
            new_result = set()
            for prefix in result:
                for suffix in factor_set:
                    new_result.add(prefix + suffix)
            result = new_result
        
        return result
    
    def _parse_factor(self) -> set:
        """
        factor -> letter | '{' expr '}'
        A single letter produces a singleton set.
        A brace group recursively parses an expression.
        """
        # If the current character is a letter, it's a singleton.
        if self.expr[self.idx].isalpha():
            letter = self.expr[self.idx]
            self.idx += 1
            return {letter}
        
        # Otherwise, it must be a '{' ... '}' group.
        # Assertion: the character is '{'
        self.idx += 1  # consume '{'
        inner_set = self._parse_expr()
        # Assertion: the character is '}'
        self.idx += 1  # consume '}'
        return inner_set