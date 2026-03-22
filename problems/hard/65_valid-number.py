class Solution:
    def isNumber(self, s: str) -> bool:
        # Track whether we have seen at least one digit in the current relevant part.
        seen_digit = False

        # A dot is only allowed in the mantissa, never after an exponent.
        seen_dot = False

        # Exponent can appear at most once, and only after a valid mantissa.
        seen_exp = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                # Any digit helps validate either the mantissa or exponent part.
                seen_digit = True

            elif ch in "+-":
                # Sign is only valid at the very beginning or immediately after e/E.
                if i > 0 and s[i - 1] not in "eE":
                    return False

            elif ch == ".":
                # Dot cannot appear twice, and cannot appear inside exponent part.
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in "eE":
                # Exponent requires a valid number before it and can appear only once.
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True

                # Reset digit requirement: exponent must contain at least one digit.
                seen_digit = False

            else:
                # Any other character is invalid under the problem constraints.
                return False

        # A valid number must end after having seen digits in the final active part.
        # This rejects cases like ".", "1e", "+", or "-.".
        return seen_digit