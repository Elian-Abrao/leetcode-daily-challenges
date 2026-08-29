from __future__ import annotations
from typing import Optional


class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        if n == 0:
            return False
        i = 0
        stack: list[str] = []

        def parse_tag_start(start: int) -> Optional[int]:
            end = code.find('>', start)
            if end == -1:
                return None
            tag_name = code[start + 1:end]
            if not (1 <= len(tag_name) <= 9):
                return None
            if not tag_name.isupper():
                return None
            if not tag_name.isalpha():
                return None
            return end + 1

        def parse_tag_end(start: int) -> Optional[tuple[str, int]]:
            end = code.find('>', start)
            if end == -1:
                return None
            tag_name = code[start + 2:end]
            if not (1 <= len(tag_name) <= 9):
                return None
            if not tag_name.isupper():
                return None
            if not tag_name.isalpha():
                return None
            return (tag_name, end + 1)

        def parse_cdata(start: int) -> Optional[int]:
            cdata_open = "<![CDATA["
            if code[start:start + len(cdata_open)] != cdata_open:
                return None
            close_pos = code.find("]]>", start + len(cdata_open))
            if close_pos == -1:
                return None
            return close_pos + 3

        if code[0] != '<':
            return False
        first_end = parse_tag_start(0)
        if first_end is None:
            return False
        tag_name = code[1:code.find('>', 0)]
        stack.append(tag_name)
        i = first_end

        while i < n:
            ch = code[i]

            if ch == '<':
                if i + 8 < n and code[i:i+9] == "<![CDATA[":
                    if not stack:
                        return False
                    new_i = parse_cdata(i)
                    if new_i is None:
                        return False
                    i = new_i
                    continue

                if i + 1 < n and code[i+1] == '/':
                    result = parse_tag_end(i)
                    if result is None:
                        return False
                    tag, new_i = result
                    if not stack or stack[-1] != tag:
                        return False
                    stack.pop()
                    i = new_i
                    if not stack and i < n:
                        return False
                    continue

                if i + 1 < n and code[i+1] != '/':
                    result = parse_tag_start(i)
                    if result is None:
                        return False
                    tag = code[i+1:code.find('>', i)]
                    stack.append(tag)
                    i = result
                    continue

                return False

            else:
                if not stack:
                    return False
                i += 1

        return not stack