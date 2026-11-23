from __future__ import annotations
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Separate logs into letter-logs and digit-logs while preserving order
        letter_logs: List[str] = []
        digit_logs: List[str] = []

        for log in logs:
            # Find the first space to split identifier from the rest
            # The second token (after identifier) determines type
            # Split once at the first space is enough
            identifier, rest = log.split(" ", 1)
            # Check if the first character of 'rest' is a digit
            # Since all tokens are space-separated, the first char of rest is the start of the second word
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter-logs: primary key = content (everything after identifier),
        # secondary key = identifier
        # Use a lambda that returns a tuple (content, identifier)
        letter_logs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        # Combine: all sorted letter-logs first, then digit-logs in original order
        return letter_logs + digit_logs