from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # Stores all valid expressions that evaluate to target
        results: List[str] = []
        n = len(num)
        if n == 0:
            return results

        # DFS helper:
        # index: current position in the string
        # path: expression built so far
        # value: evaluated value of the expression so far
        # last: value of the last operand in the expression (used for '*')
        def dfs(index: int, path: str, value: int, last: int) -> None:
            if index == n:
                # If we've consumed all digits, check if the expression matches target
                if value == target:
                    results.append(path)
                return

            for i in range(index, n):
                # Avoid numbers with leading zeros (e.g., "05", "00")
                if i > index and num[index] == '0':
                    break

                # Current operand to consider
                cur = int(num[index:i + 1])

                if index == 0:
                    # First operand: it becomes the starting path without any operator
                    dfs(i + 1, str(cur), cur, cur)
                else:
                    # Addition
                    dfs(i + 1, path + '+' + str(cur), value + cur, cur)
                    # Subtraction
                    dfs(i + 1, path + '-' + str(cur), value - cur, -cur)
                    # Multiplication: adjust value by removing last and adding last*cur
                    # This preserves the correct precedence of multiplication
                    dfs(i + 1, path + '*' + str(cur), value - last + last * cur, last * cur)

        # Start DFS from the first position
        dfs(0, "", 0, 0)
        return results