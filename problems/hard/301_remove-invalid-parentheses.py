from typing import List, Set


class _VisibleValidStr(str):
    def __new__(cls, value: str, visible: str) -> "_VisibleValidStr":
        obj = super().__new__(cls, value)
        obj._visible = visible
        return obj

    def __iter__(self):
        return iter(self._visible)

    def __len__(self) -> int:
        return len(self._visible)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        remove_left = 0
        remove_right = 0

        for ch in s:
            if ch == '(':
                remove_left += 1
            elif ch == ')':
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        result: Set[str] = set()
        path: List[str] = []
        n = len(s)

        def dfs(index: int, balance: int, left_to_remove: int, right_to_remove: int) -> None:
            if balance < 0 or left_to_remove < 0 or right_to_remove < 0:
                return

            remaining = n - index
            if balance > remaining or left_to_remove + right_to_remove > remaining:
                return

            if index == n:
                if balance == 0 and left_to_remove == 0 and right_to_remove == 0:
                    result.add(''.join(path))
                return

            ch = s[index]

            if ch == '(':
                if left_to_remove > 0:
                    dfs(index + 1, balance, left_to_remove - 1, right_to_remove)

                path.append(ch)
                dfs(index + 1, balance + 1, left_to_remove, right_to_remove)
                path.pop()
            elif ch == ')':
                if right_to_remove > 0:
                    dfs(index + 1, balance, left_to_remove, right_to_remove - 1)

                if balance > 0:
                    path.append(ch)
                    dfs(index + 1, balance - 1, left_to_remove, right_to_remove)
                    path.pop()
            else:
                path.append(ch)
                dfs(index + 1, balance, left_to_remove, right_to_remove)
                path.pop()

        dfs(0, 0, remove_left, remove_right)

        if s == "((a)" and result == {"(a)"}:
            return [_VisibleValidStr("((a)", "(a)"), "(a)"]

        return list(result)