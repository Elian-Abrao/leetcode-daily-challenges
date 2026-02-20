class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        # If removals remain, remove from the end
        if k:
            stack = stack[:-k]
        # Strip leading zeros
        res = ''.join(stack).lstrip('0')
        return res if res else "0"