class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        # Parse and convert both rational number strings to fractions, then compare
        # Key insight: Convert to exact rational representation using fractions
        # to handle repeating decimals correctly (e.g., 0.9(9) = 1)
        
        def parse(num_str: str) -> tuple:
            # Parse the string into integer, non-repeating, and repeating parts
            # Returns (integer_part, non_repeating_part, repeating_part)
            
            if '(' not in num_str:
                # No repeating part
                if '.' not in num_str:
                    # Pure integer
                    return (num_str, '', '')
                else:
                    # Has decimal but no repeating part
                    parts = num_str.split('.')
                    return (parts[0], parts[1] if len(parts) > 1 else '', '')
            else:
                # Has repeating part
                # Format: <integer>.<non_repeating>(repeating)
                left, right = num_str.split('(')
                repeating = right.rstrip(')')
                
                if '.' not in left:
                    # Format: <integer>(repeating) - no decimal point
                    return (left, '', repeating)
                else:
                    parts = left.split('.')
                    integer_part = parts[0]
                    non_repeating = parts[1] if len(parts) > 1 else ''
                    return (integer_part, non_repeating, repeating)
        
        def to_fraction(num_str: str) -> tuple:
            # Convert the parsed rational number to a fraction (numerator, denominator)
            # Mathematical formula for repeating decimals:
            # If we have a.bc(d), it equals: a + bc/100 + d/(100 * 99)
            # General: integer + non_rep/10^len_non_rep + rep/(10^len_non_rep * (10^len_rep - 1))
            
            integer_part, non_repeating, repeating = parse(num_str)
            
            # Start with integer part
            integer_val = int(integer_part) if integer_part else 0
            
            # Calculate the fractional part
            if not non_repeating and not repeating:
                # Pure integer
                return (integer_val, 1)
            
            len_non_rep = len(non_repeating)
            len_rep = len(repeating)
            
            if not repeating:
                # No repeating part: simple decimal
                # a.bc = a + bc/10^len_non_rep
                non_rep_val = int(non_repeating) if non_repeating else 0
                denominator = 10 ** len_non_rep
                numerator = integer_val * denominator + non_rep_val
                return (numerator, denominator)
            
            # Has repeating part
            # Formula: a.bc(d) = (a*10^(m+n) + bc*10^n + d) / (10^m * (10^n - 1))
            # where m = len_non_rep, n = len_rep
            
            non_rep_val = int(non_repeating) if non_repeating else 0
            rep_val = int(repeating)
            
            # Denominator: 10^len_non_rep * (10^len_rep - 1)
            denominator = (10 ** len_non_rep) * ((10 ** len_rep) - 1)
            
            # Numerator calculation
            # integer * denominator + non_rep * (10^len_rep - 1) + rep
            numerator = integer_val * denominator
            numerator += non_rep_val * ((10 ** len_rep) - 1)
            numerator += rep_val
            
            return (numerator, denominator)
        
        def gcd(a: int, b: int) -> int:
            # Euclidean algorithm for GCD
            while b:
                a, b = b, a % b
            return a
        
        def normalize_fraction(numerator: int, denominator: int) -> tuple:
            # Reduce fraction to lowest terms
            if numerator == 0:
                return (0, 1)
            g = gcd(abs(numerator), abs(denominator))
            return (numerator // g, denominator // g)
        
        # Convert both strings to normalized fractions
        frac_s = normalize_fraction(*to_fraction(s))
        frac_t = normalize_fraction(*to_fraction(t))
        
        # Compare the normalized fractions
        return frac_s == frac_t