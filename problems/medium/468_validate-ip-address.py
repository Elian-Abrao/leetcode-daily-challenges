from __future__ import annotations

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Helper to validate IPv4
        def is_ipv4(s: str) -> bool:
            parts = s.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                # Each part must be 1 to 3 digits and purely numeric
                if not part or len(part) > 3 or not part.isdigit():
                    return False
                # No leading zeros unless the part is exactly "0"
                if part[0] == '0' and len(part) != 1:
                    return False
                if int(part) > 255:
                    return False
            return True

        # Helper to validate IPv6
        def is_ipv6(s: str) -> bool:
            parts = s.split(':')
            if len(parts) != 8:
                return False
            hex_digits = set("0123456789abcdefABCDEF")
            for part in parts:
                if not part or len(part) > 4:
                    return False
                for ch in part:
                    if ch not in hex_digits:
                        return False
            return True

        # Determine type based on separators to avoid ambiguity
        if '.' in queryIP and ':' not in queryIP:
            if is_ipv4(queryIP):
                return "IPv4"
        if ':' in queryIP and '.' not in queryIP:
            if is_ipv6(queryIP):
                return "IPv6"
        return "Neither"