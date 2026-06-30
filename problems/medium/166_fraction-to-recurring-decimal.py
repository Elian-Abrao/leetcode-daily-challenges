class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator edge case
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine sign: negative if exactly one of them is negative
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values to simplify logic
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part: simple division
        integer_part = numerator // denominator
        result.append(str(integer_part))
        
        # Remainder after integer division
        remainder = numerator % denominator
        
        # If no remainder, return integer part only
        if remainder == 0:
            return "".join(result)
        
        # There is a fractional part
        result.append(".")
        
        # Track remainders and their positions to detect cycles
        # Key: remainder, Value: position in fractional part where this remainder first appeared
        remainder_map = {}
        fractional_part = []
        
        # Perform long division on the remainder
        while remainder != 0:
            # If we've seen this remainder before, we have a repeating cycle
            if remainder in remainder_map:
                # Insert opening parenthesis at the start of the cycle
                cycle_start = remainder_map[remainder]
                fractional_part.insert(cycle_start, "(")
                fractional_part.append(")")
                break
            
            # Record the position where this remainder first appears
            remainder_map[remainder] = len(fractional_part)
            
            # Long division step: multiply remainder by 10 and divide
            remainder *= 10
            digit = remainder // denominator
            fractional_part.append(str(digit))
            remainder = remainder % denominator
        
        result.extend(fractional_part)
        return "".join(result)